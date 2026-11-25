"""
Text Preprocessing Module
Handles cleaning, tokenization, and normalization of text data
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

# Download required NLTK data
try:    # if the data is already downloaded 
    nltk.data.find('tokenizers/punkt')
except LookupError:    # if the data is not downloaded then install it 
    nltk.download('punkt')

try:  # same as the before 
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


class TextPreprocessor:  #Syntax -> class Class_Name :
    """
    A class to handle all text preprocessing operations
    """
    
    def __init__(self):  # Constructor for initialize the nltk data
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.punctuation = string.punctuation
    
    
    def clean_text(self, text):
        """
        Step 1: Remove URLs, special characters, and convert to lowercase
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    
    def tokenize(self, text):
        """
        Step 2: Split text into individual words (tokens)
        """
        tokens = word_tokenize(text)
        return tokens
    
    
    def remove_stopwords(self, tokens):
        """
        Step 3: Remove common words that don't carry much meaning
        """
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        return filtered_tokens
    
    
    def stem_words(self, tokens):
        """
        Step 4: Convert words to their root form
        """
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        return stemmed_tokens
    
    
    def preprocess(self, text):
        """
        Complete preprocessing pipeline
        Combines all preprocessing steps
        """
        # Step 1: Clean text
        cleaned_text = self.clean_text(text)
        
        # Step 2: Tokenize
        tokens = self.tokenize(cleaned_text)
        
        # Step 3: Remove stopwords
        filtered_tokens = self.remove_stopwords(tokens)
        
        # Step 4: Stem words
        stemmed_tokens = self.stem_words(filtered_tokens)
        
        # Return as space-separated string
        preprocessed_text = ' '.join(stemmed_tokens)
        return preprocessed_text


# Example usage and testing
if __name__ == "__main__":     #this is like a a main method in python
    processor = TextPreprocessor()  #  "processor" is an object 
    #this is like Object creation in java just obj_name = class_name() 


    # these are the test texts that will be used to test the model
    test_texts = [
        "This product is AMAZING!!! Check it out at www.example.com #Recommend",
        "I hate this... worst purchase EVER!!!",
        "It's okay, nothing special about it."
    ]
    

    # when a string is multiplied by a int then
    # that string will be repeated that int(number) times
    print("=" * 60)
    print("TEXT PREPROCESSING DEMONSTRATION")
    print("=" * 60)
    
    for i, text in enumerate(test_texts, 1):
        print(f"\nExample {i}:")
        print(f"Original:      {text}")
        print(f"Preprocessed:  {processor.preprocess(text)}")
        print("-" * 60)
