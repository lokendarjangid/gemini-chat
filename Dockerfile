FROM python:3.10-slim

# Copy the dependencies file to the working directory

COPY requirements.txt .

# Install any dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Install google cloud in the container

RUN apt-get update 
RUN apt-get install apt-transport-https ca-certificates gnupg curl -y
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-471.0.0-linux-x86_64.tar.gz
RUN tar -xf google-cloud-cli-471.0.0-linux-x86_64.tar.gz
RUN ./google-cloud-sdk/install.sh

# Copy the service account key file
COPY service-account.json /tmp/

# Authenticate with the service account
RUN ./google-cloud-sdk/bin/gcloud auth activate-service-account --key-file=/tmp/service-account.json

RUN ./google-cloud-sdk/bin/gcloud init --console-only

# set working directory

WORKDIR /app

# Copy the rest of the code to the working directory

COPY . .

# Command to run on container start

CMD [ "python", "./src/app.py" ]