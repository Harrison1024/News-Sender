import smtplib
import requests
from app_config import *
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Total de noticias a recibir
numero_noticias = 20

# Fechas (YYYY-MM-DD)
fecha_iso = datetime.now().date().isoformat()  # Colocando la fecha de hoy sin la hora
ayer_iso = (datetime.now() - timedelta(days=1)).date().isoformat() + DESFAZE_ZONA_HORARIA # Colocando la fecha de ayer, desfaze extra para que sea desde las 6am del dia anterior(opcional)

# Ruta a la API
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything?"

# Parametros de la API
news_params ={
    "q": "AI OR cybersecurity OR programming OR technology", # Palabras a buscar
    "from" : ayer_iso,
    "to" : fecha_iso,
    "language" : "en", # Lenguaje en el que fueron escritos los articulos
    "sortBy" : "relevancy", # Orden de los articulos
    "apiKey": NEWS_API_KEY}

# Solicitud de informacion a la API
response = requests.get(url=NEWS_API_ENDPOINT, params=news_params)
response.raise_for_status()
datos = response.json()
articulos = datos["articles"][0:numero_noticias] # Agrupacion de los articulos seleccionados

# Creaciion del cuerpo del mensaje
for articulo in articulos:
    mensaje+= f"\n{articulo["source"]["name"]}"
    mensaje+= f"\n{articulo["title"]}"
    mensaje+= f"\n{articulo["description"]}"
    mensaje+= f"\n{articulo["url"]}\n\n"

# Arreglando el formato del mensaje para evitar problemas con caracteres diferentes de ASCII
msg = MIMEText(mensaje, "plain", "utf-8")
msg["Subject"] = "Artículos del día"
msg["From"] = EMAIL_ADRESS
msg["To"] = EMAIL_DESTINATARY

# Envio del correo
with smtplib.SMTP("smtp.gmail.com", port=587) as conexion: # Hacer la conexion al servidor SMTP del proveedor del correo
    conexion.starttls() # Encriptar comunicacion
    conexion.login(user= EMAIL_ADRESS, password= PASSWORD) # Iniciamos sesion en el correo
    conexion.sendmail(
        from_addr= EMAIL_ADRESS, 
        to_addrs= EMAIL_DESTINATARY, 
        msg= msg.as_string()) # Enviar el correo a la direccion especificada
