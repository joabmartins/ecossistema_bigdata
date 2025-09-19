#usa uma imagem base oficial do Python
FROM python:3.9-slim

#Define o diretório de trabalho dentro do container
WORKDIR /app

#Instala as dependência
 RUN pip install --no-cache-dir pandas

 #Copia os arquivos da aplicação
 COPY app_ch.py app.py

 #Comando para executar a aplicação
 ENTRYPOINT ["python", "app.py"]