import smtplib
from app_config import *

conexion = smtplib.SMTP("smtp.gmail.com") # Hacer la conexion al servidor SMTP del proveedor del correo
conexion.starttls() # Encriptar comunicacion
conexion.login(user= EMAIL_ADRESS, pasword= PASSWORD) # Iniciamos sesion en el correo
conexion.sendmail(from_addr= EMAIL_ADRESS, to_addrs=EMAIL_ADRESS, msg= "Hello") # Enviar el correo a la direccion especificada
conexion.close() # Cerramos la conexion
