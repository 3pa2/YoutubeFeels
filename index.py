from transformers import pipeline

# Example string
text = "I love this product! It's absolutely fantastic."

# Load a pre-trained sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis")

# Perform sentiment analysis
result = sentiment_analysis(text)

# Output sentiment result
print(result)