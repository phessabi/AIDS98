FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk --update add gcc libxml2-dev libxslt-dev libffi-dev musl-dev libgcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/
