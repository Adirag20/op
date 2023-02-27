FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /usr/app

ADD . /usr/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","-m","flask","run","--host=0.0.0.0"]