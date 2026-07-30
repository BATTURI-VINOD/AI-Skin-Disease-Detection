// ==============================
// AI Skin Disease Detection
// script.js
// ==============================

const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const form = document.getElementById("uploadForm");
const loading = document.getElementById("loading");

// ------------------------------
// Image Preview
// ------------------------------

imageInput.addEventListener("change", function () {
  const file = this.files[0];

  if (!file) {
    preview.style.display = "none";
    preview.removeAttribute("src");
    return;
  }

  const reader = new FileReader();

  reader.onload = function (e) {
    preview.src = e.target.result;
    preview.style.display = "block";
  };

  reader.readAsDataURL(file);
});

// ------------------------------
// Form Submit
// ------------------------------

form.addEventListener("submit", function (event) {
  if (imageInput.files.length === 0) {
    event.preventDefault();

    alert("Please select a skin image first.");

    return;
  }

  loading.style.display = "flex";
});

// ------------------------------
// Progress Bar Animation
// ------------------------------

window.addEventListener("load", function () {
  const progress = document.querySelector(".progress-bar");

  if (progress) {
    const width = progress.style.width;

    progress.style.width = "0%";

    setTimeout(function () {
      progress.style.width = width;
    }, 300);
  }
});
