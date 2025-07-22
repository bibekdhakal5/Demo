// Show a thank-you alert when the contact form is submitted
function submitForm(event) {
    event.preventDefault(); // Prevent page reload
    alert("Thank you for contacting Bibek College of Kathmandu!");
    document.querySelector("form").reset(); // Clear the form
}

// Show a welcome message on home page
window.onload = function () {
    if (document.body.classList.contains("home-page")) {
        alert("📚 Welcome to Bibek College of Kathmandu!");
    }

    // Show current year in footer if available
    const yearSpan = document.getElementById("current-year");
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
};
