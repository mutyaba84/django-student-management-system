FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /student_management_app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt