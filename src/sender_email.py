import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

EMAIL_SENDER=os.getenv('EMAIL_SENDER')
PASSWORD_EMAIL=os.getenv('PASSWORD_EMAIL')

def send_email(receiver, file):
    subject = "Ultimas 10 noticias de tecnologia."
    message = "Este correo esta enviado con python y tiene un archivo .PDF adjunto."

    # se crea instancia del mensaje
    msg = MIMEMultipart()
    msg['From'] = "Agente de iA (Te voy a reemplazar)"
    msg['Subject'] = subject
    msg['To'] = receiver
    msg.attach(MIMEText(message))

    # adjuntando archivo
    filepath = "./output/noticias_tecnologia.pdf"
    with open(filepath, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename = {file}')
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, PASSWORD_EMAIL)
        server.sendmail(EMAIL_SENDER, receiver, msg.as_string())
        server.quit()
        print('Correo enviado!.')


