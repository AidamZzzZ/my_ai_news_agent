import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def sumamarizer_text(text):
    """
    El modelo de iA gemini-2.5-flash genera un resumen del articulo
    """
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Resume el siguiente articulo de noticias que lo relate de manera consica: {text}"
    )
    return response.text

print(sumamarizer_text("Almost exactly six years after it launched, Apple TV is at an inflection point. In the span of a week, the streaming service rebranded itself, struck its first standalone bundle deal with a competito"))