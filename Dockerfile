# Usa una imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia sólo requirements para acelerar cache de dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Recolecta estáticos
RUN python manage.py collectstatic --noinput || echo "Collectstatic failed"


# Expone el puerto estándar de Heroku/Railway
EXPOSE 8000

# Comando para arrancar tu app con Gunicorn
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
