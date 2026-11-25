"""
Model Training Module
Trains multiple sentiment classification models and compares their performance
"""

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import os
import sys

# Import from same directory
try:
    from preprocessing import TextPreprocessor
except ImportError:
    from .preprocessing import TextPreprocessor


class SentimentModelTrainer:
    """
    Handles training and evaluation of sentiment analysis models
    """
    
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
        self.models = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.label_mapping = {'negative': 0, 'neutral': 1, 'positive': 2}
        self.reverse_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}
    
    
    def prepare_data(self, df):
        """
        Prepare data for model training:
        1. Preprocess text
        2. Convert sentiment labels to numbers
        3. Split into train and test sets
        """
        print("Preparing data...")
        
        # Preprocess all texts
        print("Preprocessing texts...")
        df['processed_text'] = df['text'].apply(self.preprocessor.preprocess)
        
        # Convert sentiment labels to numeric
        df['sentiment_encoded'] = df['sentiment'].map(self.label_mapping)
        
        # Split data: 80% training, 20% testing
        X = df['processed_text']
        y = df['sentiment_encoded']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print(f"Training set size: {len(self.X_train)}")
        print(f"Testing set size: {len(self.X_test)}")
        
        # Vectorize text using TF-IDF
        print("Vectorizing texts...")
        self.X_train_vec = self.vectorizer.fit_transform(self.X_train)
        self.X_test_vec = self.vectorizer.transform(self.X_test)
        
        print(f"Feature vector size: {self.X_train_vec.shape}")
        print("Data preparation complete!\n")
    
    
    def train_logistic_regression(self):
        """
        Train Logistic Regression model
        """
        print("Training Logistic Regression...")
        model = LogisticRegression(max_iter=200, random_state=42)
        model.fit(self.X_train_vec, self.y_train)
        self.models['logistic_regression'] = model
        return model
    
    
    def train_svm(self):
        """
        Train Support Vector Machine (SVM) model
        """
        print("Training SVM...")
        model = SVC(kernel='linear', random_state=42)
        model.fit(self.X_train_vec, self.y_train)
        self.models['svm'] = model
        return model
    
    
    def train_naive_bayes(self):
        """
        Train Naive Bayes model
        """
        print("Training Naive Bayes...")
        model = MultinomialNB()
        model.fit(self.X_train_vec, self.y_train)
        self.models['naive_bayes'] = model
        return model
    
    
    def train_all_models(self):
        """
        Train all three models
        """
        self.train_logistic_regression()
        self.train_svm()
        self.train_naive_bayes()
        print("All models trained!\n")
    
    
    def evaluate_model(self, model_name):
        """
        Evaluate a specific model and print metrics
        """
        if model_name not in self.models:
            print(f"Model '{model_name}' not found!")
            return None
        
        model = self.models[model_name]
        y_pred = model.predict(self.X_test_vec)
        
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(self.y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(self.y_test, y_pred, average='weighted', zero_division=0)
        
        print(f"\n{'='*50}")
        print(f"Model: {model_name.upper()}")
        print(f"{'='*50}")
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1-Score:  {f1:.4f}")
        
        # Confusion Matrix
        cm = confusion_matrix(self.y_test, y_pred)
        print(f"\nConfusion Matrix:")
        print(cm)
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'confusion_matrix': cm
        }
    
    
    def evaluate_all_models(self):
        """
        Evaluate all trained models and show results
        """
        print("\n" + "="*50)
        print("EVALUATING ALL MODELS")
        print("="*50)
        
        results = {}
        for model_name in self.models:
            results[model_name] = self.evaluate_model(model_name)
        
        # Find best model
        print(f"\n{'='*50}")
        print("MODEL COMPARISON")
        print(f"{'='*50}")
        
        best_model = max(results.items(), key=lambda x: x[1]['f1'])
        print(f"\nBest Model: {best_model[0]}")
        print(f"F1-Score: {best_model[1]['f1']:.4f}")
        
        return results, best_model[0]
    
    
    def save_models(self):
        """
        Save trained models and vectorizer to files
        """
        print("\nSaving models...")
        
        # Save vectorizer
        with open('vectorizer.pkl', 'wb') as f:
            pickle.dump(self.vectorizer, f)
        
        # Save models
        for model_name, model in self.models.items():
            with open(f'{model_name}_model.pkl', 'wb') as f:
                pickle.dump(model, f)
        
        print("Models saved successfully!")
    
    
    def load_models(self):
        """
        Load trained models and vectorizer from files
        """
        print("Loading models...")
        
        # Load vectorizer
        with open('vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)
        
        # Load models
        for model_file in ['logistic_regression_model.pkl', 'svm_model.pkl', 'naive_bayes_model.pkl']:
            model_name = model_file.replace('_model.pkl', '')
            try:
                with open(model_file, 'rb') as f:
                    self.models[model_name] = pickle.load(f)
            except FileNotFoundError:
                print(f"Warning: {model_file} not found")
        
        print("Models loaded successfully!")


# Example usage
if __name__ == "__main__":
    # Import data collection module
    try:
        from data_collection import load_main_dataset
    except ImportError:
        from .data_collection import load_main_dataset
    
    # Load dataset
    print("Loading dataset...")
    df = load_main_dataset()
    
    # Initialize trainer
    trainer = SentimentModelTrainer()
    
    # Prepare data
    trainer.prepare_data(df)
    
    # Train all models
    trainer.train_all_models()
    
    # Evaluate all models
    results, best_model = trainer.evaluate_all_models()
    
    # Save models
    trainer.save_models()
