document.addEventListener("DOMContentLoaded", function() {
    // Hide the splash screen after animation duration (3s in this case)
    setTimeout(function() {
        document.querySelector('.splash-screen').style.display = 'none';
    }, 3000);
})