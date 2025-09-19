# USA uma imagem base oficial do python
FROM python:3.9-slim

#Define o diretorio de trabalho dentro do container
WORKDIR /app

#instala as dependencias
RUN pip install --no-cache-dir pandas 

# Copia os arquivos da aplicação 
COPY app_ch.py app.py

# Comando para executar a aplicação
ENTRYPOINT ["python", "app.py"]