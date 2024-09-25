console.log(5 + 3);

console.log(10 - 4);

console.log(7 * 6);

console.log(20 / 5);

console.log((2 + 3) * 4);

console.log(15 - 5 / 5);

console.log(8 * 2 + 4);

console.log(100 / 4 - 10);

console.log((6 + 2) * (3 - 1));

console.log(10 + 5 * 2 - 3 / 1);

const greeting = "გამარჯობა";

let name = "დავით";

// ტექსტის აწყობა
let message = greeting + ", " + name + "!";
console.log(message);

name = "ნიკა";
message = greeting + ", " + name + "!";
console.log(message);

// JavaScript Module 1 Quiz

// 1. ცვლადების გამოცხადება და გამოყვანა
let a = 10; // ცვლადი 'a' -ის გამოცხადება და 10-ის მინიჭება
let b = 20; // ცვლადი 'b' -ის გამოცხადება და 20-ის მინიჭება
console.log("a:", a); // 'a' ცვლადის მნიშვნელობის გამოყვანა
console.log("b:", b); // 'b' ცვლადის მნიშვნელობის გამოყვანა

// 2. მათემატიკური ოპერაციები
let sum = a + b; // 'a' და 'b' -ის ჯამის გამოთვლა
console.log("Sum:", sum); // ჯამის გამოყვანა

let product = a * b; // 'a' და 'b' -ის გამრავლების გამოთვლა
console.log("Product:", product); // გამრავლების შედეგის გამოყვანა

// 3. პირობა და ციკლები
if (a < b) {
  // თუ 'a' ნაკლებია 'b'-ზე
  console.log("a is less than b"); // შესაბამისი შეტყობინების გამოყვანა
} else {
  console.log("a is not less than b"); // წინააღმდეგ შემთხვევაში
}

// 4. for ციკლის გამოყენება
for (let i = 1; i <= 5; i++) {
  // 1-დან 5-მდე რიცხვების გაშვება
  console.log("Current number:", i); // მიმდინარე რიცხვის გამოყვანა
}

// 5. ფუნქციის შექმნა
function greet(name) {
  // ფუნქცია 'greet' -ის შექმნა
  return "Hello, " + name + "!"; // დაბრუნების მნიშვნელობა + ოპერატორის გამოყენებით
}

// ფუნქციის გამოძახება
console.log(greet("saba")); // 'greet' ფუნქციის გამოძახება და შედეგის გამოყვანა

// 6. მასივების გამოყენება
let numbers = [1, 2, 3, 4, 5]; // ცვლადი 'numbers' -ის გამოცხადება და მასივის შექმნა
console.log("Numbers array:", numbers); // მასივის გამოყვანა

// 7. ობიექტების შექმნა
let person = {
  // ობიექტი 'person' -ის შექმნა
  name: "giorgi", // თვისება 'name'
  age: 30, // თვისება 'age'
};
console.log("Person:", person); // ობიექტის გამოყვანა

// 8. ობიექტის თვისების წვდომა
console.log("Person's name:", person.name); // 'name' თვისების გამოყვანა
console.log("Person's age:", person.age); // 'age' თვისების გამოყვანა
