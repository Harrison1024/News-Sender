import smtplib
from app_config import *

conexion = smtplib.SMTP("smtp.gmail.com", port=587) # Hacer la conexion al servidor SMTP del proveedor del correo, se incluye el puerto por temas de actualizacion del SMTP
conexion.starttls() # Encriptar comunicacion
conexion.login(user= EMAIL_ADRESS, password= PASSWORD) # Iniciamos sesion en el correo
conexion.sendmail(from_addr= EMAIL_ADRESS, to_addrs=EMAIL_DESTINATARY, msg= "Subject:Hello\nHow are you?") # Enviar el correo a la direccion especificada
conexion.close() # Cerramos la conexion
