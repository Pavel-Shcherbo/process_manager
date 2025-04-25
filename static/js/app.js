// static/js/app.js
document.addEventListener("DOMContentLoaded", () => {
  const img = document.getElementById("previewImg");
  if (!img) return;
  let scale = 1;
  document.getElementById("zoomIn").onclick = () => {
    scale += 0.1;
    img.style.transform = `scale(${scale})`;
  };
  document.getElementById("zoomOut").onclick = () => {
    scale = Math.max(0.2, scale - 0.1);
    img.style.transform = `scale(${scale})`;
  };
});
