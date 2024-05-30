import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

remitente = os.getenv('USER')
destinatario = 'damianalejandrofirst@gmail.com'
asunto = 'Tienes una cita pendiente'


msg = MIMEMultipart()
msg['Subjetc'] = asunto
msg['From'] = remitente
msg['To'] = destinatario

with open('sendEmail.html', 'r') as archivo:
    html = archivo.read()

msg.attach(MIMEText(html, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remitente, os.getenv('PASSWORD'))

server.sendmail(remitente, destinatario, msg.as_string())


server.quit()