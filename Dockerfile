# 1. Imagen base
FROM python:3.9-slim

# 2. Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Copiar y instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código
COPY . /app/

# 6. Copiar y dar permisos al entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 7. Expone el puerto
EXPOSE 8000

# 8. Arranca con nuestro script
ENTRYPOINT ["/entrypoint.sh"]
