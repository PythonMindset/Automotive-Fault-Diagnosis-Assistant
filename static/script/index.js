const textarea = document.getElementById('userInput');
const placeholder = document.querySelector('.placeholder');
const diagnoseBtn = document.getElementById('diagnoseBtn');
const loaderOverlay = document.getElementById('loaderOverlay');
const form = document.getElementById('diagnoseForm');

// helper to update placeholder visibility
function updatePlaceholder() {
    const hasText = textarea.value.trim().length > 0;
    if (hasText) {
        placeholder.classList.add('hidden');
    } else {
        placeholder.classList.remove('hidden');
    }
}

// run on input
textarea.addEventListener('input', updatePlaceholder);

// ensure initial state is correct (in case textarea has value on load)
document.addEventListener('DOMContentLoaded', updatePlaceholder);

// Button click
diagnoseBtn.addEventListener('click', () => {
    const text = textarea.value.trim();

    if (!text) {
        alert("Please describe your vehicle problem before diagnosing.");
        return;
    }

    // Show loader overlay and blur background
    loaderOverlay.style.display = "flex";
    document.querySelector('.container').style.filter = "blur(5px)";

    // Submit form after 5 seconds
    setTimeout(() => {
        form.submit();
    }, 2000);
});