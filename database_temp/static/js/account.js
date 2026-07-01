/* jshint esversion: 6 */
function previewProfilePic(event) {
    const image = document.getElementById("profilePic");

    if (event.target.files && event.target.files[0]) {
        image.src = URL.createObjectURL(event.target.files[0]);
    }
}

function editProfile() {
    window.location.href = "/edit_profile";
}

function createPost() {
    window.location.href = "/create_post";
}

function toggleComment(postId) {

    const box =
        document.getElementById(
            "commentBox" + postId
        );

    if (box.style.display === "block") {
        box.style.display = "none";
    } else {
        box.style.display = "block";
    }
}

//const profilePic = document.getElementById("profilePic");
const profilePic = document.getElementById("profilePic");
console.log(profilePic);

const changeBtn = document.getElementById("changeBtn");
const uploadBtn = document.getElementById("uploadBtn");
const profileInput = document.getElementById("profileInput");

if (profilePic) {

    profilePic.addEventListener("click", function () {
        changeBtn.style.display = "inline-block";
    });

    changeBtn.addEventListener("click", function () {
        profileInput.click();
    });

    profileInput.addEventListener("change", function () {
        if (profileInput.files.length > 0) {
            uploadBtn.style.display = "inline-block";
        }
    });

}