# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the default command to run pytest
CMD ["sh", "-c", "$TEST_COMMAND"]