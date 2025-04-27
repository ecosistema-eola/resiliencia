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


# Expone el puerto (no es obligatorio, pero es buena práctica)
EXPOSE 8000

# Arranca Gunicorn, usando $PORT si viene de Railway, o 8000 por defecto


HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl --fail http://localhost:${PORT:-8000}/healthz/ || exit 1
