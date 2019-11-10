FROM python:3

ENV FLASK_ENV=production

ENV ENVFLASK_DEBUG=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5001

CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
