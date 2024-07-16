# Use the official Playwright image as a base image
FROM mcr.microsoft.com/playwright/python:v1.45.0-focal

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi && \
    pip install pytest allure-pytest junit-xml

# Set PYTHONPATH to include the project root
ENV PYTHONPATH=/app

# Run the tests and generate reports
CMD . venv/bin/activate && pytest tests/test_table.py --alluredir=/app/allure-results --junitxml=/app/junit-results.xml && allure generate /app/allure-results -o /app/allure-report && chown -R root:root /app/allure-results /app/allure-report /app/junit-results.xml