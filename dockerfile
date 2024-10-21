FROM python:3.9-slim-buster
RUN apt-get update && apt-get install ffmpeg -y
RUN mkdir /qbot
WORKDIR /qbot
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]