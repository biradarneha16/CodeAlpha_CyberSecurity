"""Train a basic text classifier from a labelled CSV dataset."""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="emails.csv", help="CSV with text and label columns")
    parser.add_argument("--text-column", default="text")
    parser.add_argument("--label-column", default="label", help="Labels should be phishing/safe or 1/0")
    args = parser.parse_args()
    df = pd.read_csv(args.data)
    if args.text_column not in df or args.label_column not in df:
        raise SystemExit(f"CSV must contain columns: {args.text_column}, {args.label_column}")
    df = df[[args.text_column, args.label_column]].dropna()
    if df[args.label_column].nunique() < 2: raise SystemExit("Dataset must contain at least two classes.")
    x_train, x_test, y_train, y_test = train_test_split(
        df[args.text_column].astype(str), df[args.label_column].astype(str),
        test_size=0.2, random_state=42, stratify=df[args.label_column].astype(str))
    model = Pipeline([("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1, stop_words="english")),
                      ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions, zero_division=0))
    ConfusionMatrixDisplay.from_predictions(y_test, predictions, xticks_rotation="vertical")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=150)
    print("Saved confusion_matrix.png")
    print("Note: results depend on dataset quality; this model is a triage aid, not a guarantee.")
if __name__ == "__main__": main()
