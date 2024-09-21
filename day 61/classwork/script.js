//string
//integer
//float
//boolean

//console.log(100);
//console.log(10 + 14);
//console.log(100 / 2);
//console.log("hello" + "world");
let btnstyle = document.querySelector(".btn");
function changestyle() {
  btnstyle.style.color = "red";
  btnstyle.style.backgroundcolor = "yellow";
  btnstyle.textContent = "clicked";
  btnstyle.style.width = "500px";
  btnstyle.style.height = "150px";
  btnstyle.style.border = "0px";
  btnstyle.style.borderRadius = "53px";
  btnstyle.style.cursor = "pointer";
  btnstyle.style.transition = "1.5s";
}
