"""
Data Collection and Preparation Module
Uses the sentiment_dataset.csv as the main training dataset
"""

import pandas as pd
import os


def load_main_dataset():
    """
    Loads the main sentiment_dataset.csv file
    Returns a pandas DataFrame
    """
    # Try to load from src directory first, then root
    dataset_paths = [
        os.path.join(os.path.dirname(__file__), 'sentiment_dataset.csv'),
        'sentiment_dataset.csv',
        os.path.join('src', 'sentiment_dataset.csv')
    ]
    
    for path in dataset_paths:
        if os.path.exists(path):
            print(f"Loading dataset from: {path}")
            df = pd.read_csv(path)
            return df
    
    raise FileNotFoundError("sentiment_dataset.csv not found!")


def save_dataset(df, filename='dataset.csv'):
    """
    Saves the dataset to a CSV file
    """
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")
    print(f"Total samples: {len(df)}")
    print(f"Sentiment distribution:\n{df['sentiment'].value_counts()}")
    return filename


def load_dataset(filename='dataset.csv'):
    """
    Loads the dataset from a CSV file
    """
    # Try multiple locations
    if os.path.exists(filename):
        df = pd.read_csv(filename)
    elif os.path.exists(os.path.join('..', filename)):
        df = pd.read_csv(os.path.join('..', filename))
    else:
        # Fall back to main dataset
        df = load_main_dataset()
    
    return df


if __name__ == "__main__":
    # Load and display the main dataset
    print("Loading main sentiment dataset...")
    dataset = load_main_dataset()
    
    print("\nDataset preview:")
    print(dataset.head(10))
    
    print("\nDataset statistics:")
    print(f"Total samples: {len(dataset)}")
    print(f"\nSentiment distribution:")
    print(dataset['sentiment'].value_counts())
    
    print("\nSample texts by sentiment:")
    for sentiment in ['positive', 'negative', 'neutral']:
        print(f"\n{sentiment.upper()} examples:")
        samples = dataset[dataset['sentiment'] == sentiment].head(3)
        for idx, row in samples.iterrows():
            print(f"  - {row['text']}")
