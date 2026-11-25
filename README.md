# Sentiment Analysis System

A complete machine learning-based sentiment analysis system that classifies text into positive, negative, or neutral sentiments.

## Quick Start

### For Web Application

```bash
# 1. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train models first (if not done yet)
python run_cli.py
# Select Option 4 (Create Dataset)
# Select Option 1 (Train Models)

# 4. Run web application
python app.py
```

Then open your browser to: `http://localhost:5000`

### For Command-Line Interface

```bash
# 1. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run CLI
python run_cli.py
```

## Project Structure

```
SentimentAnalysis/
├── src/                        # Source code folder
│   ├── main.py                 # CLI interface
│   ├── data_collection.py      # Dataset creation
│   ├── preprocessing.py        # Text preprocessing
│   ├── model_training.py       # Model training
│   └── sentiment_predictor.py  # Predictions
├── templates/                  # HTML templates
│   └── index.html              # Web interface
├── static/                     # CSS and JavaScript
│   ├── style.css
│   └── script.js
├── app.py                      # Flask web application
├── run_cli.py                  # CLI launcher script
├── requirements.txt            # Dependencies
├── *.pkl                       # Trained models
└── dataset.csv                 # Training data
```

## Features

✓ **Web Interface**: Simple browser-based sentiment analysis  
✓ **CLI Interface**: Interactive command-line menu  
✓ **Multiple ML Models**: Logistic Regression, SVM, Naive Bayes  
✓ **Text Preprocessing**: Tokenization, stopword removal, stemming  
✓ **Confidence Scoring**: Probability estimates for predictions  
✓ **Real-time Analysis**: Instant predictions  

## Usage - Web Application

1. Open browser to `http://localhost:5000`
2. Enter text in the textarea
3. Click "Analyze Sentiment"
4. View results with confidence score

## Usage - Command Line

```bash
python run_cli.py
```

### CLI Menu Options:
- **Option 1**: Train models (requires dataset)
- **Option 2**: Predict sentiment of text
- **Option 3**: Test with sample texts
- **Option 4**: Create and save new dataset
- **Option 5**: Exit

## Example Usage

```
Input:  "This product is absolutely amazing!"
Output: 
  Sentiment: POSITIVE
  Confidence: 94.2%

Input:  "Worst purchase ever, complete waste."
Output: 
  Sentiment: NEGATIVE
  Confidence: 91.5%
```

## Model Performance

- **Logistic Regression**: ~93% accuracy (Recommended)
- **SVM**: ~87% accuracy
- **Naive Bayes**: ~80% accuracy

## Documentation

- **README.md** - This file, quick start guide
- **WEB_APP_GUIDE.md** - Detailed web application setup
- **PROJECT_REPORT.md** - Full technical details and methodology
- **SETUP_GUIDE.txt** - Step-by-step setup instructions
- **EXAMPLES.txt** - Example inputs and outputs

## Requirements

- Python 3.8+
- 500MB disk space
- 2GB RAM

## Libraries Used

- Flask - Web framework
- NLTK - Natural Language Processing
- scikit-learn - Machine Learning
- pandas - Data manipulation
- NumPy - Numerical computing

---

**Get Started:** Run `python app.py` for web interface or `python run_cli.py` for CLI!
