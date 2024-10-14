function divisibilityChecker() {
  const number = parseInt(prompt("Enter a number:"));

  if (isNaN(number)) {
    alert("Please enter a valid number.");
    return;
  }

  if (number % 15 === 0) {
    alert("FizzBuzz");
  } else if (number % 3 === 0) {
    alert("Fizz");
  } else if (number % 5 === 0) {
    alert("Buzz");
  } else {
    alert(number);
  }
}

divisibilityChecker();
