# FROM is to say what image we're basing this off of. Like extending.
# Alpine refers to Alpine Linux (lightweight base image).
FROM python:3.7-alpine

# This label will state who is the maintainer
LABEL maintainer="tom"

# Setting an enviroment variable to 1.
# This tells python to run in unbuffered mode which is recommended in docker containers.
# Doesn't let python buffer outputs, it just prints them directly.
ENV PYTHONUNBUFFERED 1

# Copy from the repo requirements file to the image within requirements.txt
COPY ./requirements.txt /requirements.txt
# Installs from the images requirements
RUN pip install -r /requirements.txt

# Creates directory
RUN mkdir /app
# Make default directory in the container. Any app we run in the container will start
# from this location (unless specificied otherwise).
WORKDIR /app
# Copy local app file to the container
COPY ./app /app

# Creates a user (-D a use for running applications only).
RUN adduser -D user
# Switches docker to the user
# If this is not done, it runs from the root account. Not recommended.
# Security wise, you'd have root access if someone got in.
# Having a user with just application access limits scope for a potential attacker.
USER user