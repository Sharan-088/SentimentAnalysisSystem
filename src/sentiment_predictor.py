"""
Sentiment Predictor Module
Uses trained models to predict sentiment of new text
"""

import pickle
import os
import sys

# Import from same directory
try:
    from preprocessing import TextPreprocessor
except ImportError:
    from .preprocessing import TextPreprocessor


class SentimentPredictor:
    """
    Loads trained models and makes sentiment predictions
    """
    
    def __init__(self, model_name='logistic_regression'):
        self.preprocessor = TextPreprocessor()
        self.model_name = model_name
        self.model = None
        self.vectorizer = None
        self.reverse_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}
        self.load_model()
    
    
    def load_model(self):
        """
        Load the saved model and vectorizer
        """
        try:
            # Load vectorizer
            with open('vectorizer.pkl', 'rb') as f:
                self.vectorizer = pickle.load(f)
            
            # Load model
            with open(f'{self.model_name}_model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            
            print(f"Model '{self.model_name}' loaded successfully!")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print("Make sure the model files exist. Run model_training.py first.")
    
    
    def predict(self, text):
        """
        Predict sentiment of given text
        Returns sentiment label and confidence
        """
        if self.model is None or self.vectorizer is None:
            return "Error: Model not loaded"
        
        # Preprocess text
        processed_text = self.preprocessor.preprocess(text)
        
        # Vectorize
        text_vector = self.vectorizer.transform([processed_text])
        
        # Predict
        prediction = self.model.predict(text_vector)[0]
        
        # Get confidence (probability)
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(text_vector)[0]
            confidence = max(probabilities)
        else:
            confidence = None
        
        # Map to sentiment label
        sentiment = self.reverse_mapping[prediction]
        
        return {
            'text': text,
            'sentiment': sentiment,
            'confidence': confidence,
            'prediction_code': prediction
        }
    
    
    def predict_batch(self, texts):
        """
        Predict sentiment for multiple texts
        """
        results = []
        for text in texts:
            result = self.predict(text)
            results.append(result)
        return results


# Example usage and testing
if __name__ == "__main__":
    print("="*60)
    print("SENTIMENT ANALYSIS PREDICTION")
    print("="*60)
    
    # Initialize predictor
    predictor = SentimentPredictor(model_name='logistic_regression')
    
    # Test examples
    test_texts = [
        "This product is absolutely amazing! I love it!",
        "Terrible quality, waste of money.",
        "It's okay, nothing special.",
        "Best purchase I've made in years!",
        "Complete disappointment and frustration.",
    ]
    
    print("\nMaking predictions...\n")
    for text in test_texts:
        result = predictor.predict(text)
        print(f"Text: {result['text']}")
        print(f"Sentiment: {result['sentiment'].upper()}")
        if result['confidence']:
            print(f"Confidence: {result['confidence']:.4f}")
        print("-" * 60)
