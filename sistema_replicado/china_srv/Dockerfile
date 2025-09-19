# usa uma imagem bae oficial do python
from python:3.9-slim

#define o diretoria de trabalho dentro do contanier
WORKDIR /app
  
#instala as depedencias
RUN pip install --no-cache-dir pandas

#copia os arquivos da aplicaçao
COPY app_ch.py app.py

#comando para executar a aplicaçao
ENTRYPOINT ["python",  "app.py"]