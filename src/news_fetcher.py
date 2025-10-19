import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# obtiene las 10 ultimas noticias sobre tecnologia en estados unidos (Solo en ingles)
def get_news(api_key):
    newsapi = NewsApiClient(api_key)
    tech_articles = newsapi.get_top_headlines(category='technology', country='us')
    return tech_articles['articles'][:10]
