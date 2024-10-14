function checkAgeGroup() {
  const age = prompt("თქვენი ასაკი:");

  if (!age || isNaN(age) || age < 0) {
    alert("გთხოვთ, სწორად შეიყვანოთ ასაკი.");
    return;
  }

  let ageGroup;

  if (age <= 12) {
    ageGroup = "ბავშვი";
  } else if (age <= 19) {
    ageGroup = "თინეიჯერი";
  } else if (age <= 64) {
    ageGroup = "ზრდასრული";
  } else {
    ageGroup = "უფროსი";
  }

  alert(`თქვენ ხართ: ${ageGroup}`);
}

checkAgeGroup();
