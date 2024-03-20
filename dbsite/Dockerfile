FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD . /code/
#ADD .env.docker /code/.env

RUN mkdir -p /code/static


CMD python manage.py migrate


ENV APP_NAME=RAD_ELEMENTS

#RUN pip install -r requirements.txt

CMD gunicorn dbsite.wsgi:application -b radcomponents.ru:8000
#CMD python manage.py runserver 0.0.0.0:8000

