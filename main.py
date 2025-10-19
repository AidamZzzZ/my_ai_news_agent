import os
import schedule
import time
from dotenv import load_dotenv
from src.news_fetcher import get_news
from src.summarizer import summarizer_text
from src.pdf_generator import create_pdf
from src.sender_email import send_email

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL_RECIEVER=os.getenv('EMAIL_RECIEVER')

def main():
    articles = get_news(NEWS_API_KEY)
    
    summarizer_text_list = []

    for article in articles:
        if article['content']:
            summarizer = summarizer_text(article['content'])
            summarizer_text_list.append({"titulo": article['title'], 'resumen': summarizer, 'url': article['url']})
        else:
            summarizer = summarizer_text(article.get('description', ''))
            summarizer_text_list.append({'titulo': article['title'], 'resumen': summarizer, 'url': article['url']})

    create_pdf(summarizer_text_list)
    print("PDF creado")
    send_email(EMAIL_RECIEVER, "noticias_tecnologia.pdf")
    print("Noticias enviadas por correo")

# ejectura la funcion main cada dia a las 6:00 am
schedule.every().day.at("06:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)