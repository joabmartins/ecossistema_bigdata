#usa imagem basse ofc do python
FROM python:3.9-slim
#define o diretotrio de trabalho dentro do container
WORKDIR /app
#instala a dependência
RUN pip install --no-cache-dir pandas
#Copiar os arquivos da aplicação
COPY app_ch.py app.py
#executar a aplicação
ENTRYPOINT ["Python", "app.py"]