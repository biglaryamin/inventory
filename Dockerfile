FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for psycopg2
RUN apt-get update \
    && apt-get install -y python3-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the container at /app/
COPY requirements.txt /app/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy the rest of the application code
COPY ./anbar_project /app/
