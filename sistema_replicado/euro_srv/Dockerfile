FROM python:3.9-slim

WORKDIR /app

#instala as dependencias
RUN pip install --no-cache-dir pandas 

# Copia os arquivos da aplicação 
COPY app_eu.py app.py

# Comando para executar a aplicação
ENTRYPOINT ["python", "app.py"]