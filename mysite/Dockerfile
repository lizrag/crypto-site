FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update \
# psycopg2 dependencies
&& apk add --virtual build-deps gcc python3-dev musl-dev
# Pillow dependencies\
# https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000