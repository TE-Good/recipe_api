# FROM is to say what image we're basing this off of. Like extending a class.
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

# Installs postgres database
# `apk add` = package manager name and the instruction to add a package
# `--update` = update register before adding
# `--no-cache` = dont store the registery index to our dockerfile, meaning less data
# in our container which should be considered best practice. Want smallest footprint,
# and less requirements and unknown issues.
RUN apk add --update --no-cache postgresql-client jpeg-dev

# Install temporary packages (to create smallest footprint possible).
# `--virtual` sets up an alias that we can use to remove to locate and remove later.
# `\` is to continue the command on a new line for formatting.
# These additional requirements where not trivially found, but through trial and error
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# Installs from the images requirements
RUN pip install -r /requirements.txt

# Deletes the temporary packages through the alias
RUN apk del .tmp-build-deps

# Creates directory
RUN mkdir /app
# Make default directory in the container. Any app we run in the container will start
# from this location (unless specificied otherwise).
WORKDIR /app
# Copy local app file to the container
COPY ./app /app

# Create a directory for our images
RUN mkdir -p /vol/web/media

# Create a directory for our static files
RUN mkdir -p /vol/web/static

# Creates a user (-D a use for running applications only).
RUN adduser -D user

# Sets ownership of the vol directories to our user
# -R = recursive
RUN chown -R user:user /vol

# Owner(user) can do everything, and the rest can read and execute
RUN chmod -R 755 /vol/web

# Switches docker to the user
# If this is not done, it runs from the root account. Not recommended.
# Security wise, you'd have root access if someone got in.
# Having a user with just application access limits scope for a potential attacker.
USER user