FROM python:3.10.3-slim-buster

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

ENTRYPOINT ["python3", "src/main.py"]