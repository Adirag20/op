FROM python:3.8-slim

WORKDIR /usr/app

COPY ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 5000

CMD ["python","-u","app.py"]