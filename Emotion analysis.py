import pandas as pd
from textblob import TextBlob

# Input: A set of movie reviews
reviews = [
    "This movie was terrible. The acting was poor and the storyline was predictable.",
    "I loved this movie! The acting was great and the storyline was unexpected.",
    "The acting was decent and the storyline was okay, but nothing special.",
    "This movie was a complete disaster. The acting was terrible and the storyline was boring."
]

# Preprocessing
reviews = [review.lower() for review in reviews]

# Sentiment Analysis
results = []
for review in reviews:
    analysis = TextBlob(review)
    sentiment = analysis.sentiment.polarity
    if sentiment < 0:
        sentiment_label = "Negative"
    elif sentiment == 0:
        sentiment_label = "Neutral"
    else:
        sentiment_label = "Positive"
    results.append({
        "review": review,
        "sentiment_score": sentiment,
        "sentiment_label": sentiment_label
    })

# Store results in a Pandas dataframe
df = pd.DataFrame(results)

# Output: Sentiment analysis results
print(df)
