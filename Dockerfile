FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /usr/app

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ ./

EXPOSE 80

CMD ["python3","-m","flask","run","--host=0.0.0.0"]