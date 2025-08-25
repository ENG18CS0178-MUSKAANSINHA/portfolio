// Update footer year automatically
document.addEventListener("DOMContentLoaded", () => {
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
});

// Optional: highlight active nav link
const currentPath = window.location.pathname;
document.querySelectorAll(".nav-link").forEach(link => {
  if (link.getAttribute("href") === currentPath) {
    link.classList.add("active");
  }
});
