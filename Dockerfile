# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libdrm2 \
    libxkbcommon0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install-deps && playwright install

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Run pytest with the TEST_COMMAND environment variable
CMD ["sh", "-c", "$TEST_COMMAND"]