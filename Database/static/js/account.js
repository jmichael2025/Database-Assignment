function editProfile() {
    alert("Profile editing coming soon!");
}

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