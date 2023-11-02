FROM python:latest

WORKDIR /app

COPY requirements.txt ./
COPY fastapi_entrypoint.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "./fastapi_entrypoint.py" ]