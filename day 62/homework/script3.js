const image = document.querySelector(".image");
const resizeButton = document.getElementById("resizeButton");

image.style.cssText =
  "border: 2px solid black; padding: 10px; width: 300px; height: 200px;";

resizeButton.addEventListener("click", () => {
  image.style.width = "400px";
  image.style.height = "300px";
});
