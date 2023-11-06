# docker build -t ubuntu-python-runtime:3.10 .
# Use the official Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Update the package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    ffmpeg \
    && ln /usr/bin/python3 /usr/bin/python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the entrypoint command
CMD [ "python3", "your_script.py" ]