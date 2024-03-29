# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

RUN python manage.py migrate

RUN useradd django
RUN chown -R django /code
USER django

EXPOSE 9999
CMD python manage.py runserver 0.0.0.0:9999
