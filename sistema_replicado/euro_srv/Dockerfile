FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas

COPY app_eu.py app.py 

ENTRYPOINT [ "python", "app.py"]