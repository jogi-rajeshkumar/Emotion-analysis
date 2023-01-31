from textblob import TextBlob

# Input: A movie review
review = "This movie was terrible. The acting was poor and the storyline was predictable."

# Preprocessing
review = review.lower()

# Sentiment Analysis
analysis = TextBlob(review)
sentiment = analysis.sentiment.polarity

# Output: Sentiment score
if sentiment < 0:
    print("Negative")
elif sentiment == 0:
    print("Neutral")
else:
    print("Positive")
