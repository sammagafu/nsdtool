# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /code
COPY . /code/
