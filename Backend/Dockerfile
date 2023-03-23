FROM python:3.8-slim

WORKDIR /usr/app

COPY ./requirements.txt ./

# OpenCV dependencies
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install libzbar0 -y 

# installing flask dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install deepface

COPY ./ ./

EXPOSE 5000

CMD ["python","-u","app.py"]