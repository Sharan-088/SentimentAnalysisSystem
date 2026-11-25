# Getting Started with Sentiment Analysis System

## 📌 What You Have

This project includes:
- ✅ Complete sentiment analysis system
- ✅ Web application (Flask)
- ✅ Command-line interface
- ✅ Machine learning models (Logistic Regression, SVM, Naive Bayes)
- ✅ Comprehensive documentation

---

## 🚀 Two Ways to Use This System

### Option 1: Web Application (Recommended)
**Best for:** Easy, visual interface in your browser

### Option 2: Command-Line Interface
**Best for:** Terminal users, batch processing

---

## 📋 Setup Steps (Do This Once)

### Step 1: Activate Virtual Environment

**Windows PowerShell:**
```powershell
cd "c:\Users\Sharan Raja\OneDrive\Documents\Documents\Intern\Task 2\SentimentAnalysis"
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
cd "c:\Users\Sharan Raja\OneDrive\Documents\Documents\Intern\Task 2\SentimentAnalysis"
venv\Scripts\activate.bat
```

You should see `(venv)` at the start of your command line.

### Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- NLTK (text processing)
- Scikit-learn (machine learning)
- Pandas & NumPy (data handling)

**Wait:** 2-3 minutes for installation

### Step 3: Train Models (First Time Only)

```bash
python run_cli.py
```

Then follow these steps:
1. Press `4` → Create Dataset
2. Press `1` → Train Models (wait ~60 seconds)
3. Press `5` → Exit

**What this does:** Creates training data and trains 3 ML models

---

## 🌐 Using the Web Application

### Start the Server

```bash
python app.py
```

### Access the Website

Open your browser and go to:
```
http://localhost:5000
```

### Using the Interface

1. **Enter Text**: Type or paste text in the text box
2. **Click "Analyze Sentiment"**: Get instant results
3. **View Results**: 
   - Sentiment: POSITIVE / NEGATIVE / NEUTRAL
   - Confidence: How sure the model is (0-100%)
   - Original text displayed

### Try Sample Texts

Click on these buttons for quick tests:
- 😊 **Positive Example**
- 😞 **Negative Example**
- 😐 **Neutral Example**

### Stop the Server

Press `Ctrl+C` in the terminal

---

## 💻 Using the Command-Line Interface

### Start CLI

```bash
python run_cli.py
```

### Menu Options

```
1. Train models         → Train/retrain the ML models
2. Predict sentiment    → Enter text and get prediction
3. Test samples         → Test with pre-loaded examples
4. Create dataset       → Generate training data
5. Exit                 → Close the program
```

### Example Usage

```
> Enter your choice: 2

> Enter text to analyze: This product is amazing!

------------------------------------------------------------
Text: This product is amazing!
Sentiment: POSITIVE
Confidence: 95.23%
------------------------------------------------------------
```

---

## 📁 Project Structure

```
SentimentAnalysis/
│
├── src/                      # All Python code
│   ├── main.py               # CLI application
│   ├── data_collection.py    # Creates datasets
│   ├── preprocessing.py      # Cleans text
│   ├── model_training.py     # Trains models
│   └── sentiment_predictor.py # Makes predictions
│
├── templates/                # HTML files
│   └── index.html            # Web page
│
├── static/                   # CSS & JavaScript
│   ├── style.css             # Styling
│   └── script.js             # Interactive features
│
├── app.py                    # Web application
├── run_cli.py                # CLI launcher
│
├── dataset.csv               # Training data
├── vectorizer.pkl            # Text vectorizer
├── logistic_regression_model.pkl  # Best model
├── svm_model.pkl             # Alternative model
└── naive_bayes_model.pkl     # Alternative model
```

---

## 🔧 Troubleshooting

### Problem: "Model not loaded" error

**Solution:** Train models first
```bash
python run_cli.py
# Press 4, then 1
```

### Problem: Port 5000 already in use

**Solution:** Change port in `app.py` (line 115):
```python
app.run(debug=True, port=5001)  # Change to 5001
```

Then access: `http://localhost:5001`

### Problem: ModuleNotFoundError

**Solution:** Install requirements
```bash
pip install -r requirements.txt
```

### Problem: Virtual environment won't activate

**Solution (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📊 Understanding Results

### Sentiments

- **POSITIVE** 😊: Happy, satisfied, recommending
  - Example: "This is amazing! I love it!"
  
- **NEGATIVE** 😞: Unhappy, disappointed, angry
  - Example: "Terrible product, waste of money"
  
- **NEUTRAL** 😐: Factual, balanced, no strong emotion
  - Example: "The product works as described"

### Confidence Score

- **90-100%**: Very confident ✅
- **70-89%**: Confident ✓
- **50-69%**: Moderate confidence ⚠️
- **Below 50%**: Uncertain ❓

### Model Accuracy

- Logistic Regression: **~93%** (Best, used by default)
- SVM: **~87%**
- Naive Bayes: **~80%**

---

## 📖 Documentation Files

| File | What It Contains |
|------|-----------------|
| **GETTING_STARTED.md** | This file - quick start guide |
| **README.md** | Project overview |
| **WEB_APP_GUIDE.md** | Detailed web app instructions |
| **PROJECT_REPORT.md** | Complete technical documentation |
| **SETUP_GUIDE.txt** | Detailed setup steps |
| **EXAMPLES.txt** | Example predictions and outputs |
| **STEP_BY_STEP_EXECUTION.md** | Full execution workflow |

---

## ⚡ Quick Commands Reference

```bash
# Activate venv
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Train models (CLI)
python run_cli.py

# Run web app
python app.py

# Access web app
http://localhost:5000
```

---

## 🎯 What to Do Next

### For Testing:
1. ✅ Start web app: `python app.py`
2. ✅ Open browser: `http://localhost:5000`
3. ✅ Try different texts
4. ✅ Check confidence scores

### For Learning:
1. 📖 Read `PROJECT_REPORT.md` for how it works
2. 🔍 Check `EXAMPLES.txt` for sample outputs
3. 💻 Explore `src/` folder to see the code

### For Submission:
1. 📦 Zip the entire folder
2. 📧 Include all files
3. 📝 Mention both web and CLI interfaces

---

## 🎓 Key Features to Highlight

✨ **Dual Interface**: Web + Command-line  
✨ **Multiple Models**: 3 ML algorithms compared  
✨ **High Accuracy**: 93% with Logistic Regression  
✨ **Real-time**: Instant predictions  
✨ **User-friendly**: Clean, simple interface  
✨ **Well-documented**: Comprehensive guides  
✨ **Production-ready**: Organized code structure  

---

## 💡 Tips

1. **Better Predictions**: Use complete sentences
2. **Clear Sentiment**: Avoid sarcasm or mixed emotions
3. **Test Various Texts**: Try reviews, tweets, comments
4. **Check Confidence**: Low confidence = ambiguous text

---

## 🎉 You're Ready!

**To start using:**
```bash
python app.py
```

**Then open:** http://localhost:5000

**Have fun analyzing sentiments!** 🚀

---

## 📧 For Help

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Review **WEB_APP_GUIDE.md** for web app issues
3. Review **SETUP_GUIDE.txt** for setup issues
4. Check console logs for error messages

---

**Last Updated:** 2024
**Author:** Sentiment Analysis Project
**Technologies:** Python, Flask, Scikit-learn, NLTK
