# Use an official Python runtime as a parent image
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# Set the working directory to /code
WORKDIR /code 
ADD . .
# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /code
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# $ docker exec -it ndstool python manage.py migrate
