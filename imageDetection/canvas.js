const canvas = document.body.querySelector("#canvas");
const ctx = canvas.getContext("2d");
const increaseBtn = document.body.querySelector(".plus");
const decreaseBtn = document.body.querySelector(".minus");
const sizeEL = document.body.querySelector(".value");
const colorEl = document.body.querySelector(".color");
const clearEl = document.body.querySelector(".clear");

let x, y;
let size = 10;
let color = "Black";
let isPressed = false;

// Create an Image object and set its source to the saved image
const image = new Image();
image.src = "blank.jpeg";

// Once the image is loaded, draw it on the canvas
image.onload = function () {
  ctx.drawImage(image, 0, 0);
};
canvas.addEventListener("mousedown", (e) => {
  isPressed = true;

  x = e.offsetX;
  y = e.offsetY;
});
canvas.addEventListener("mouseup", (e) => {
  isPressed = false;

  x = undefined;
  y = undefined;
});
canvas.addEventListener("mousemove", (e) => {
  if (isPressed) {
    const x2 = e.offsetX;
    const y2 = e.offsetY;
    drawCircle(x2, y2);
    drawLine(x, y, x2, y2);

    x = x2;
    y = y2;
  }
});

function drawCircle(x, y) {
  ctx.beginPath();
  ctx.arc(x, y, size, 0, Math.PI * 2, true);
  ctx.fillStyle = color;
  ctx.fill();
}
function drawLine(x1, y1, x2, y2) {
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.strokeStyle = color;
  ctx.lineWidth = size * 2;
  ctx.stroke();
}

function updateSizeOnScreen() {
  sizeEL.innerText = size;
}

increaseBtn.addEventListener("click", () => {
  size += 5;

  if (size > 50) {
    size = 50;
  }

  updateSizeOnScreen();
});

decreaseBtn.addEventListener("click", () => {
  size -= 5;

  if (size < 5) {
    size = 5;
  }

  updateSizeOnScreen();
});

colorEl.addEventListener("change", (e) => (color = e.target.value));

clearEl.addEventListener("click", () =>
  ctx.clearRect(0, 0, canvas.width, canvas.height)
);

// drawCircle(50,50)
// drawLine(50,50,50,100)
