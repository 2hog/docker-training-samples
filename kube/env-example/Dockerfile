# Base buildpack
FROM python:3.6

# Install dependencies
RUN pip install pipenv==2018.7.1
COPY Pipfile* /usr/src/app/
WORKDIR /usr/src/app
RUN pipenv install --deploy --system

# Copy code
COPY ./ /usr/src/app
ENV WEB_CONCURRENCY=2

# Web command
CMD gunicorn --bind=0.0.0.0:5000 app:app
