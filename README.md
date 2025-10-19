# 📰🤖 Agente de Noticias de IA

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/AidamZzzZ/my_ai_news_agent)

---

## Descripción

**Agente de Noticias de IA** es una herramienta automatizada que recopila las 10 noticias más recientes sobre tecnología en Estados Unidos, genera un resumen conciso usando la API de Gemini de Google, crea un informe PDF profesional y lo envía automáticamente por correo electrónico. Todo desde Python y utilizando prácticas modernas de automatización y procesamiento de lenguaje natural.

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Créditos y agradecimientos](#créditos-y-agradecimientos)
- [Enlaces útiles](#enlaces-útiles)
- [Licencia](#licencia)

---

## Características

- Obtención automática de noticias del sector tecnológico de EE. UU. vía NewsAPI
- Resumen inteligente de cada noticia usando Gemini (Google Generative AI)
- Generación de PDF atractivo y compatible (FPDF)
- Envío del PDF generado al correo especificado (sistema SMTP)
- Configuración mediante variables de entorno para mayor seguridad

---

## Requisitos

- Python 3.10 o superior
- Claves API para NewsAPI y Gemini (Google Generative AI)
- Cuenta de correo compatible con SMTP (ej: Gmail)
- Dependencias especificadas en `requirements.txt`

---

## Instalación

```bash
# 1. Clona este repositorio
git clone https://github.com/<YOUR_GITHUB_USER>/<YOUR_REPO>.git
cd my_ai_news_agent

# 2. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt
```

Configura un archivo `.env` en la raíz del proyecto con las siguientes variables:

```ini
NEWS_API_KEY=tu_clave_newsapi
gemini_API_KEY=tu_clave_gemini
EMAIL_SENDER=correo@ejemplo.com
PASSWORD_EMAIL=contraseña_de_aplicacion
EMAIL_RECIEVER=destinatario@ejemplo.com
```

---

## Uso

1. Ejecuta el script principal:

```bash
python main.py
```
2. El proceso obtendrá, resumirá y enviará el PDF de noticias automáticamente al correo especificado.
3. El PDF se almacenará también en la carpeta `/output/`.

---

## Estructura del Proyecto

```
my_ai_news_agent/
├── main.py                 # Punto de entrada del sistema
├── requirements.txt        # Dependencias del proyecto
├── output/
│   └── noticias_tecnologia.pdf  # Informe PDF generado
└── src/
    ├── news_fetcher.py     # Módulo para obtener noticias
    ├── summarizer.py       # Módulo de resumen con Gemini
    ├── pdf_generator.py    # Generador de PDF profesional
    ├── sender_email.py     # Envío de email con adjunto
    └── __init__.py
```

---

## Créditos y agradecimientos

- [NewsAPI](https://newsapi.org/)
- [Google Gemini/Generative AI](https://ai.google.dev/)
- [FPDF](https://pyfpdf.github.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Shields.io](https://shields.io/) para insignias

---

## Enlaces útiles

- [Repositorio en GitHub](https://github.com/AidamZzzZ)
- [Documentación de NewsAPI](https://newsapi.org/docs)
- [Documentación de Gemini](https://ai.google.dev/docs)
- [Guía de README Profesional (ES)](https://coding-boot-camp.github.io/full-stack/es/github/professional-readme-guide/)

---

## Licencia

Este proyecto está licenciado bajo términos de la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
