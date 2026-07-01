/* jshint esversion: 6 */
function displayHamberger() {
    const nav = document.getElementById("navRight");
    const icon = document.querySelector(".icon i");

    nav.classList.toggle("responsive");

    if (nav.classList.contains("responsive")) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");
    } else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
    }
}