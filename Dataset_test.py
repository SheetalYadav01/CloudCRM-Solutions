import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Try using 'latin1' encoding to read the CSV file
    df = pd.read_csv(r"C:\Users\Amrutha\CMPE 272\test.csv", encoding='latin1')

    # Analyze sentiments for the first 10 rows
    for index, row in df.head(10).iterrows():
        text = row['text']  # Replace 'text' with the actual column name
        sentiment = analyze_sentiment(text)
        print(f"Text: \"{text}\"\nSentiment: {sentiment}\n")
