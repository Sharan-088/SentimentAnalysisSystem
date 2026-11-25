// Analyze sentiment function
async function analyzeSentiment() {
    const textInput = document.getElementById('textInput');
    const text = textInput.value.trim();
    
    // Hide previous results and errors
    document.getElementById('resultContainer').style.display = 'none';
    document.getElementById('errorContainer').style.display = 'none';
    
    // Validate input
    if (!text) {
        showError('Please enter some text to analyze.');
        return;
    }
    
    // Show loading
    document.getElementById('loading').style.display = 'block';
    
    try {
        // Make API request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        // Hide loading
        document.getElementById('loading').style.display = 'none';
        
        if (data.success) {
            displayResult(data);
        } else {
            showError(data.error || 'An error occurred during analysis.');
        }
        
    } catch (error) {
        document.getElementById('loading').style.display = 'none';
        showError('Failed to connect to the server. Please try again.');
        console.error('Error:', error);
    }
}

// Display result function
function displayResult(data) {
    const resultContainer = document.getElementById('resultContainer');
    const sentimentBadge = document.getElementById('sentimentBadge');
    const sentimentText = document.getElementById('sentimentText');
    const progressFill = document.getElementById('progressFill');
    const confidenceValue = document.getElementById('confidenceValue');
    const analyzedText = document.getElementById('analyzedText');
    
    // Set sentiment
    sentimentText.textContent = data.sentiment.toUpperCase();
    sentimentBadge.className = 'sentiment-badge ' + data.sentiment_class;
    
    // Set confidence
    const confidence = data.confidence || 0;
    progressFill.style.width = confidence + '%';
    confidenceValue.textContent = confidence.toFixed(2) + '%';
    
    // Set analyzed text
    analyzedText.textContent = data.text;
    
    // Show result
    resultContainer.style.display = 'block';
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Show error function
function showError(message) {
    const errorContainer = document.getElementById('errorContainer');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorContainer.style.display = 'block';
    
    // Scroll to error
    errorContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Use sample text function
function useSample(sampleText) {
    const textInput = document.getElementById('textInput');
    textInput.value = sampleText;
    
    // Auto-analyze
    analyzeSentiment();
}

// Enter key to submit
document.addEventListener('DOMContentLoaded', function() {
    const textInput = document.getElementById('textInput');
    
    if (textInput) {
        textInput.addEventListener('keydown', function(event) {
            // Ctrl+Enter or Cmd+Enter to submit
            if (event.key === 'Enter' && (event.ctrlKey || event.metaKey)) {
                event.preventDefault();
                analyzeSentiment();
            }
        });
    }
});

// Clear button functionality (if needed)
function clearInput() {
    document.getElementById('textInput').value = '';
    document.getElementById('resultContainer').style.display = 'none';
    document.getElementById('errorContainer').style.display = 'none';
}
