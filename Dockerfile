FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# 1) Dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 2) Entrypoint (con permisos)
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 3) Resto del código
COPY . /app/

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
