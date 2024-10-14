function temperatureAdvice() {
  const temperature = prompt("შეიყვანეთ მიმდინარე ტემპერატურა °C:");

  if (isNaN(temperature)) {
    alert("გთხოვთ, შეიყვანოთ სწორი რიცხვი.");
    return;
  }

  if (temperature < 0) {
    alert("it's freezing outside!");
  } else if (temperature <= 20) {
    alert("it's chilly. Wear a kacket.");
  } else if (temperature <= 30) {
    alert("ot's warm. Light clothins is fine.");
  } else {
    alert("it;s hot. Stay hydrated!");
  }
}

temperatureAdvice();
