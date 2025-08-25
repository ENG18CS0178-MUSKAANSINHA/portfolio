import os
import json
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# --- Load project data once ---
with open(os.path.join("data", "projects.json"), "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)


# slug → project map for detail pages
PROJECT_MAP = {p["slug"]: p for p in PROJECTS}


@app.context_processor
def inject_globals():
    return {
"SITE_NAME": "Muskaan Sinha",
"TAGLINE": "Senior Software Developer · GenAI & Automation",
"GITHUB": "https://github.com/ENG18CS0178-MUSKAANSINHA",
"LINKEDIN": "https://www.linkedin.com/in/muskaan-sinha-093581189/",
"EMAIL": "muskaan.sinha2708@gmail.com",
}


@app.route("/")
def home():
    featured = [p for p in PROJECTS if p.get("featured")] [:3]
    return render_template("index.html", featured=featured)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/project/<slug>")
def project_detail(slug):
    project = PROJECT_MAP.get(slug)
    if not project:
        abort(404)   # stop here if not found
    return render_template("project_detail.html", project=project)



@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')


@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.static_folder, "sitemap.xml", mimetype="application/xml")



@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)