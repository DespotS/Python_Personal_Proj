from textblob import TextBlob
from newspaper import Article
import nltk


url='https://edition.cnn.com/2024/04/13/business/lights-technology-sleep-wellness/index.html'
article = Article(url)

article.download()
article.parse()
article.nlp() #preparing it for natural language processing


text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # from -1 to 1

def sentiment_scale(sentiment):
    if sentiment >= 0.8:
        return "Very positive"
    elif sentiment >=0.6:
        return "Positive"
    elif sentiment >=0.4:
        return "Slightly positive"
    elif sentiment >=0.2:
        return "Neutral"
    elif sentiment >=0:
        return "Slightly negative"
    elif sentiment >=-0.2:
        return "Negative"
    elif sentiment >= -0.4:
        return "Very negative"
    else:
        return "Extremely negative"
    
sentiment_message = sentiment_scale(sentiment)

print("The sentiment for this article is: ", sentiment_message)
