"""
Flask Web Application for Sentiment Analysis
Provides a user-friendly web interface for sentiment prediction
"""

from flask import Flask, render_template, request, jsonify
import os
import sys

# Add src folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from sentiment_predictor import SentimentPredictor

app = Flask(__name__)

# Initialize the sentiment predictor
try:
    predictor = SentimentPredictor(model_name='logistic_regression')
    model_loaded = True
except Exception as e:
    print(f"Error loading model: {e}")
    model_loaded = False


@app.route('/')
def home():
    """
    Home page route
    Renders the main interface
    """
    return render_template('index.html', model_loaded=model_loaded)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction API endpoint
    Accepts text input and returns sentiment prediction
    """
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.',
            'success': False
        })
    
    try:
        # Get text from request
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'error': 'Please enter some text to analyze.',
                'success': False
            })
        
        # Make prediction
        result = predictor.predict(text)
        
        # Prepare response
        response = {
            'success': True,
            'text': result['text'],
            'sentiment': result['sentiment'],
            'confidence': round(result['confidence'] * 100, 2) if result['confidence'] else None,
            'sentiment_class': result['sentiment'].lower()
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'error': f'Error during prediction: {str(e)}',
            'success': False
        })


@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """
    Batch prediction endpoint
    Accepts multiple texts and returns predictions for all
    """
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.',
            'success': False
        })
    
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        
        if not texts:
            return jsonify({
                'error': 'Please provide texts to analyze.',
                'success': False
            })
        
        # Make predictions for all texts
        results = []
        for text in texts:
            if text.strip():
                result = predictor.predict(text)
                results.append({
                    'text': result['text'],
                    'sentiment': result['sentiment'],
                    'confidence': round(result['confidence'] * 100, 2) if result['confidence'] else None,
                    'sentiment_class': result['sentiment'].lower()
                })
        
        return jsonify({
            'success': True,
            'results': results
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Error during batch prediction: {str(e)}',
            'success': False
        })


if __name__ == '__main__':
    # Check if models exist
    if not os.path.exists('logistic_regression_model.pkl'):
        print("\n" + "="*60)
        print("WARNING: Model files not found!")
        print("Please train the models first by running:")
        print("  python main.py")
        print("  Then select Option 1: Train models")
        print("="*60 + "\n")
    
    # Run the Flask app
    print("\n" + "="*60)
    print("Starting Sentiment Analysis Web Application...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
