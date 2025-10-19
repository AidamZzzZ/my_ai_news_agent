import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def summarizer_text(text):
    """
    El modelo de iA gemini-2.5-flash genera un resumen del articulo
    """
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Resume el siguiente articulo de noticias que lo relate de manera consica: {text}"
    )
    return response.text