# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the environment variable for non-interactive apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system dependencies and clean up apt cache to reduce image size
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for the application and set the working directory in the container
WORKDIR /app

# Copy your application code into the container
COPY . .

# Ensure bash.sh has executable permissions
# RUN chmod +x bash.sh

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Command to run your application (assuming bash.sh is your entry point)
CMD gunicorn app:app & python3 -m main.py
