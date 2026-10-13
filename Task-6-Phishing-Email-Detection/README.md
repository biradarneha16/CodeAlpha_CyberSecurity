# Task 6 — Phishing Email Detection (Scikit-learn)

Train a TF-IDF + Logistic Regression baseline on a labelled email dataset.

## Dataset
Place a legally obtained dataset in this directory as `emails.csv` with columns `text,label`. Labels may be `phishing/safe` or `1/0`. Do not commit personal, confidential, or real user email data.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python phishing_model.py --data emails.csv
```

Outputs accuracy, precision/recall/F1 and `confusion_matrix.png`. Use a stratified holdout split. Report dataset source, class balance, and test results in any submission; do not claim high accuracy before running on a representative dataset. URL/keyword feature engineering can be added as a next step.
