"""
Main Command-Line Interface
Interactive sentiment analysis system
"""

import sys
import os

# Import from same directory
try:
    from sentiment_predictor import SentimentPredictor
    from data_collection import load_main_dataset, save_dataset, load_dataset
    from model_training import SentimentModelTrainer
except ImportError:
    from .sentiment_predictor import SentimentPredictor
    from .data_collection import load_main_dataset, save_dataset, load_dataset
    from .model_training import SentimentModelTrainer


def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("        SENTIMENT ANALYSIS SYSTEM")
    print("="*60)


def print_menu():
    """Print main menu options"""
    print("\nMain Menu:")
    print("1. Train models (use sentiment_dataset.csv)")
    print("2. Predict sentiment of text")
    print("3. Test with sample texts")
    print("4. View dataset information")
    print("5. Exit")
    print("-"*60)


def option_train_models():
    """Train models on dataset"""
    print("\n--- Training Models ---")
    
    try:
        # Load the main dataset (sentiment_dataset.csv with 1500 samples)
        print("Loading sentiment_dataset.csv...")
        df = load_main_dataset()
        
        print(f"Loaded {len(df)} samples")
        print(f"Sentiment distribution:\n{df['sentiment'].value_counts()}\n")
        
        # Initialize trainer
        trainer = SentimentModelTrainer()
        
        # Prepare data
        trainer.prepare_data(df)
        
        # Train all models
        print("\nTraining models...")
        trainer.train_all_models()
        
        # Evaluate models
        results, best_model = trainer.evaluate_all_models()
        
        # Save models
        trainer.save_models()
        
        print("\n✓ Models trained and saved successfully!")
        
    except FileNotFoundError:
        print("Error: dataset.csv not found!")
        print("Please create a dataset first (Option 4)")
    except Exception as e:
        print(f"Error during training: {e}")


def option_predict_sentiment():
    """Predict sentiment of user input"""
    print("\n--- Predict Sentiment ---")
    
    try:
        predictor = SentimentPredictor(model_name='logistic_regression')
        
        print("Enter text to analyze (or 'back' to return to menu):")
        
        while True:
            text = input("\n> ").strip()
            
            if text.lower() == 'back':
                break
            
            if not text:
                print("Please enter some text.")
                continue
            
            result = predictor.predict(text)
            
            print("\n" + "-"*60)
            print(f"Text: {result['text']}")
            print(f"Sentiment: {result['sentiment'].upper()}")
            if result['confidence']:
                print(f"Confidence: {result['confidence']:.2%}")
            print("-"*60)
    
    except FileNotFoundError:
        print("Error: Model files not found!")
        print("Please train models first (Option 1)")
    except Exception as e:
        print(f"Error during prediction: {e}")


def option_test_samples():
    """Test with predefined sample texts"""
    print("\n--- Testing with Sample Texts ---")
    
    try:
        predictor = SentimentPredictor(model_name='logistic_regression')
        
        samples = [
            "This product is absolutely fantastic!",
            "Worst purchase ever, completely useless.",
            "It's an average product, nothing special.",
            "I absolutely love this! Highly recommended!",
            "Terrible quality and poor customer service.",
            "The product works as described.",
            "Amazing quality and fast delivery!",
            "Disappointing and not worth the price.",
        ]
        
        print(f"\nAnalyzing {len(samples)} sample texts...\n")
        
        for i, text in enumerate(samples, 1):
            result = predictor.predict(text)
            confidence_str = f" (Confidence: {result['confidence']:.2%})" if result['confidence'] else ""
            print(f"{i}. [{result['sentiment'].upper()}]{confidence_str}")
            print(f"   \"{text}\"")
            print()
    
    except FileNotFoundError:
        print("Error: Model files not found!")
        print("Please train models first (Option 1)")
    except Exception as e:
        print(f"Error during testing: {e}")


def option_create_dataset():
    """Display dataset information and prepare it for training"""
    print("\n--- Dataset Information ---")
    
    try:
        df = load_main_dataset()
        
        print("\nDataset loaded successfully!")
        print(f"Total samples: {len(df)}")
        print(f"\nSentiment distribution:")
        print(df['sentiment'].value_counts())
        
        print("\nSample texts:")
        for sentiment in ['positive', 'negative', 'neutral']:
            print(f"\n{sentiment.upper()}:")
            sample = df[df['sentiment'] == sentiment].iloc[0]['text']
            print(f"  '{sample}'")
        
        # Save a copy to working directory for training
        save_dataset(df, 'dataset.csv')
        print("\n✓ Dataset ready for training!")
        
    except Exception as e:
        print(f"Error loading dataset: {e}")


def main():
    """Main application loop"""
    print_header()
    print("Welcome to the Sentiment Analysis System!")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            option_train_models()
        elif choice == '2':
            option_predict_sentiment()
        elif choice == '3':
            option_test_samples()
        elif choice == '4':
            option_create_dataset()
        elif choice == '5':
            print("\nThank you for using Sentiment Analysis System!")
            print("Goodbye!\n")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        sys.exit(0)
