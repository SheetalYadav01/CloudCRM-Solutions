import pandas as pd
from textblob import TextBlob

#Jenkins pipeline test
def analyze_sentiment(text):
   if not isinstance(text, str):  # Check if the text is not a string
       return "Unknown"  # Or handle as needed
   blob = TextBlob(text)
   polarity = blob.sentiment.polarity


   if polarity > 0:
       return "Positive"
   elif polarity < 0:
       return "Negative"
   else:
       return "Neutral"


# Step 1: Load the CSV file into a DataFrame with specified encoding
file_path = "test.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1') 


# Clean column names to remove extra spaces
df.columns = df.columns.str.strip()


# Convert non-string values to empty strings
df['text'] = df['text'].astype(str)


# Step 2: Preview the dataset (optional)
print(df.head())  # Prints the first 5 rows of the dataframe


# Step 3: Perform sentiment analysis on the 'text' column
if 'text' in df.columns:
   df['Sentiment'] = df['text'].apply(analyze_sentiment) 


   # Step 4: Output the results
   print(df[['text', 'Sentiment']].head())
else:
   print("The CSV does not have a column named 'text'. Please check the column names.")


