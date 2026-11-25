"""
Retrain Models Script
This script properly trains the models using the full sentiment_dataset.csv (1500 samples)
"""

import sys
sys.path.insert(0, 'src')

from src.data_collection import load_main_dataset
from src.model_training import SentimentModelTrainer

print("="*60)
print("RETRAINING MODELS WITH FULL DATASET")
print("="*60)

# Load the main dataset
print("\n1. Loading sentiment_dataset.csv...")
df = load_main_dataset()

print(f"✓ Loaded {len(df)} samples")
print(f"\nSentiment distribution:")
print(df['sentiment'].value_counts())

# Initialize trainer
print("\n2. Initializing trainer...")
trainer = SentimentModelTrainer()

# Prepare data
print("\n3. Preparing data...")
trainer.prepare_data(df)

# Train all models
print("\n4. Training models...")
print("   This will take 1-2 minutes...\n")
trainer.train_all_models()

# Evaluate models
print("\n5. Evaluating models...")
results, best_model = trainer.evaluate_all_models()

# Save models
print("\n6. Saving models...")
trainer.save_models()

print("\n" + "="*60)
print("✓ MODELS RETRAINED SUCCESSFULLY!")
print("="*60)
print(f"\nBest Model: {best_model}")
print("\nYou can now use:")
print("  - python app.py (for web interface)")
print("  - python run_cli.py (for command-line)")
print("\nThe models should now work correctly!")
