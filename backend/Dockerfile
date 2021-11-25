FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

CMD python server.py