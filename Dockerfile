# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Run pytest with the TEST_COMMAND environment variable
CMD ["sh", "-c", "$TEST_COMMAND"]