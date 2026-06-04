const imageInput = document.getElementById("image");
const imagePreview = document.getElementById("imagePreview");

imageInput.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = "block";
        };

        reader.readAsDataURL(file);
    }
});

document.getElementById("postForm").addEventListener("submit", function (e) {
    e.preventDefault();

    alert("Post submitted!");

    // Later you'll send the data to Flask using fetch()
});