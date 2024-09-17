from textblob import TextBlob
import pandas as pd

# Supongamos que tenemos un DataFrame 'tweets' con una columna 'text' que contiene los tweets
tweets = pd.DataFrame({'text': ["I love Python!", "Pandas is great", "I hate bugs"]})

# Análisis de sentimiento
tweets['sentiment'] = tweets['text'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)
print(tweets)