import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(api_key):
    """
        obtiene las 10 ultimas noticias sobre tecnologia en estados unidos (Solo en ingles)
    """
    newsapi = NewsApiClient(api_key)
    tech_articles = newsapi.get_top_headlines(category='technology', country='us')
    return tech_articles['articles'][:10]

print(get_news(NEWS_API_KEY))