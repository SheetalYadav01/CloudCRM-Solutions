import pandas as pd
from textblob import TextBlob
# from sklearn.preprocessing import LabelEncoder
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from scipy.sparse import hstack
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score


def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text string and returns whether it is
    Positive, Negative, or Neutral based on the polarity score.
    
    :param text: str : The text string to be analyzed.
    :return: str : Sentiment of the text (Positive, Negative, Neutral).
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Analyze sentiment polarity
    sentiment_polarity = blob.sentiment.polarity
    
    # Determine the sentiment category
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "It's okay, not great but not bad either.",
        "I'm feeling neutral about this.",
        "Absolutely fantastic! Highly recommend.",
        "I don't like this at all.",
        "The weather is average today.",
        "Could be better, but it's not terrible.",
        "I'm very happy with the results!",
        "This is disappointing."
    ]
    
    # Run sentiment analysis on each test case
    for text in test_cases:
        sentiment = analyze_sentiment(text)
        print(f"Text: \"{text}\"\nSentiment: {sentiment}\n")