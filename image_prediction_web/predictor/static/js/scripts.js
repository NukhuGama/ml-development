// File: predictor/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const imageInput = document.getElementById('image-input');
    const clearButton = document.getElementById('clear-button');
    
    // Add event listeners
    imageInput.addEventListener('change', previewImage);
    clearButton.addEventListener('click', clearForm);
    
    function previewImage(event) {
        const input = event.target;
        const reader = new FileReader();
        
        // Reset the preview image each time a new image is selected
        const preview = document.getElementById('preview');
        if (preview) {
            preview.classList.remove('hidden');
            preview.src = "";  // Clear any previous image preview
        }
        
        // Hide the entire prediction results section if it exists
        const predictionResults = document.getElementById('prediction-results');
        if (predictionResults) {
            predictionResults.style.display = 'none';
        }
        
        reader.onload = function() {
            preview.src = reader.result;  // Set new image as preview
            preview.style.display = 'block';  // Show the image preview
        };
        
        if (input.files && input.files[0]) {
            reader.readAsDataURL(input.files[0]);  // Read new image
        }
    }
    
    function clearForm() {
        // Reset the file input
        document.getElementById('image-input').value = '';
        
        // Hide the preview image
        const preview = document.getElementById('preview');
        if (preview) {
            preview.style.display = 'none';
            preview.src = '';
        }
        
        // Hide prediction results if they exist
        const predictionResults = document.getElementById('prediction-results');
        if (predictionResults) {
            predictionResults.style.display = 'none';
        }
    }
});