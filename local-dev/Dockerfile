FROM python:3.6-alpine

WORKDIR /usr/src/app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --system --deploy

COPY . /usr/src/app