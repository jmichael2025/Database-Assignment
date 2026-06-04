/*jshint esversion: 6 */

const form = document.getElementById("signUpForm");
const password = document.getElementById ("password");
const confirmPassword = document.getElementById("confirmPassword");
const passwordError = document.getElementById ("passwordError");
const confirmError = document.getElementById ("confirmError");

form.addEventListener ("submit",function (e) {

  let valid= true;

  const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;

      if(!passwordPattern.test(password.value)){
        passwordError.textContent= 
        "Password must be 8+ chars, include uppercase, lowercase & number";
        passwordError.style.visibility= "visible";
        valid=false; 
      } else {
        passwordError.style.visibility="hidden";
      }

      if (password.value !== confirmPassword.value) {
        confirmError.textContent ="Passwords do not match";
        confirmError.style.visibility = "visible";
        valid=false;
      } else {
        confirmError.style.visibility = "hidden";
      }
      
      if(!valid)
      {
        e.preventDefault();
      }
});