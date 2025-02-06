# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto de la app
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
