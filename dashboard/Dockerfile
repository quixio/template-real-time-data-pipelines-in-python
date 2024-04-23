FROM python:3.10.3-slim-buster

# Install build dependencies, including gcc
RUN apt-get update \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND="noninteractive"
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONPATH="/app"

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file to the container and install dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN python3 -m pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=80"]