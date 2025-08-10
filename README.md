# 📧 Daily Tech News Email Sender

Este script en Python obtiene las noticias más relevantes de las últimas 24 horas sobre **Inteligencia Artificial**, **Programación**, **Avances Tecnológicos** y **Ciberseguridad**, y las envía automáticamente a tu correo electrónico.

## 🚀 Características
- Obtiene artículos recientes desde [NewsAPI.org](https://newsapi.org/).
- Filtra noticias en inglés sobre temas tecnológicos clave.
- Ordena los artículos por relevancia.
- Envía un correo con **fuente**, **título**, **descripción** y **enlace**.
- Compatible con cuentas de Gmail (o cualquier proveedor con SMTP).

---

## 📋 Requisitos
- **Python 3.8+**
- Una cuenta en [NewsAPI.org](https://newsapi.org/) para obtener una API Key.
- Una cuenta de correo que permita SMTP (por defecto configurada para Gmail).
- Librerías:
  ```bash
  pip install requests
````

---

## ⚙️ Configuración

**Crear `app_config.py`** en la carpeta raíz con el siguiente contenido:

   ```python
   NEWS_API_KEY = "tu_api_key_de_newsapi"
   EMAIL_ADRESS = "tu_correo@gmail.com"
   PASSWORD = "tu_contraseña_o_app_password"
   EMAIL_DESTINATARY = "correo_destino@gmail.com"
   DESFAZE_ZONA_HORARIA = ""  # Opcional: ajustar horas si es necesario
   ```

   ⚠️ **Nota sobre Gmail**: Si usas Gmail, debes habilitar "Contraseñas de aplicación" desde tu cuenta para usar SMTP de forma segura.

---

## 🖥 Uso

Ejecuta el script:

```bash
python main.py
```

Automáticamente:

1. Consulta las noticias más recientes de las últimas 24h.
2. Filtra por temas: `AI`, `cybersecurity`, `programming`, `technology`.
3. Envía un correo con los artículos al destinatario configurado.

---

## 🛠 Personalización

* Cambia las **palabras clave** en la variable `news_params["q"]` para otros temas.
* Ajusta `numero_noticias` para recibir más o menos artículos.
* Cambia el idioma modificando `language` (`"en"`, `"es"`, etc.).
* Modifica el rango de fechas con `ayer_iso` y `fecha_iso`.

---

## 📌 Ejemplo de correo enviado

```
TechCrunch
AI Startup raises $50M to expand
The company focuses on AI solutions for healthcare.
https://www.techcrunch.com/article...

The Hacker News
Major cybersecurity breach affects millions
Details on the latest vulnerability...
https://thehackernews.com/article...
```

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

