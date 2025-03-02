document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorMessage = document.getElementById('errorMessage');
    const shareButton = document.getElementById('shareButton');

    if (form) {
        form.addEventListener('submit', function(e) {
            // Show loading indicator
            loadingIndicator.classList.remove('d-none');
            errorMessage.classList.add('d-none');

            // Let the form submit naturally - no need to prevent default
            // The server will handle the redirect
        });
    }

    if (shareButton) {
        shareButton.addEventListener('click', async function() {
            const predictionContent = document.getElementById('predictionResult').innerText;
            try {
                await navigator.clipboard.writeText(predictionContent);
                alert('Prediction copied to clipboard! Share your fate with others!');
            } catch (err) {
                showError('Failed to copy prediction');
            }
        });
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('d-none');
        loadingIndicator.classList.add('d-none');
    }
});