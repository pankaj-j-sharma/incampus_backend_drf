# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
# RUN git clone https://github.com/gothinkster/django-realworld-example-app.git /drf_src

# create root directory for our project in the container
RUN mkdir /api

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /api

# Copy the current directory contents into the container at /music_service
ADD . /api/

# Install any needed packages specified in requirements.txt
RUN pip install -r _incampus_backend_drf/requirements.txt

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
