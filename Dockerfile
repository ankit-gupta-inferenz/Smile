# Start with a base image of Ubuntu
FROM ubuntu:latest

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install necessary packages
RUN apt-get install -y python3-pip \
    && pip3 install django==3.2.8 \
    && pip3 install kafka \
    && apt-get install -y libmysqlclient-dev \
    && apt-get install -y apache2 libapache2-mod-wsgi-py3 \
    && apt-get install -y apache2-utils

# Copy the Smile directory to the container
COPY Smile /Smile

# Set working directory
WORKDIR /Smile

EXPOSE 8080

# Configure Apache and Django
RUN apachectl configtest && service apache2 restart \
    && pip3 install numpy kafka-python

# Start Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
