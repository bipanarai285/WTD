function checkEligibility() {
    let age = prompt("Please enter your age:");
    let message;
  
    if (age === null || age === "") {
      message = "Please enter a valid age.";
    } else if (isNaN(age) || age < 0) {
      message = "The age is invalid.";
    } else if (age >= 18) {
      message = "You are eligible to vote.";
    } else {
      message = "You are not eligible to vote.";
    }
  
    document.getElementById("p1").innerText = message;
  }