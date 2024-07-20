document.getElementById("sortButton").addEventListener("click", function () {
    var popup = document.getElementById("popup");
    if (popup.style.display === "none" || popup.style.display === "") {
        popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
});

document.getElementById("resetButton").addEventListener("click", function () {
    console.log("Reset clicked!");
    // Add your reset functionality here
    document.getElementById("popup").style.display = "none";
});

document.getElementById("applyButton").addEventListener("click", function () {
    console.log("Apply clicked!");
    // Add your apply functionality here
    document.getElementById("popup").style.display = "none";
});
