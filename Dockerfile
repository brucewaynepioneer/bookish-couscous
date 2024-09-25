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

# Ensure bash.sh has executable permissions and convert line endings from Windows to Unix
RUN chmod +x bash.sh && sed -i 's/\r$//' bash.sh

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the Gunicorn server with logging enabled
CMD flask run -h 0.0.0.0 -p 8000 & python3 -m main
