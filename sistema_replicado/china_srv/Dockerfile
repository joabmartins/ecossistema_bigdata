# Usa uma imagem base ofical do python
FROM python:3.9-slim

# Define o diretório do trabalho dentro do continer
WORKDIR /app

# Instala as dependências
RUN pip install --no-cache-dir pandas

# Copia os arquivos da aplicação
COPY app_ch.py app.py 

# Comando para executar a aplicação
ENTRYPOINT ["python", "app.py"]