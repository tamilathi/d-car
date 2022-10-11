# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
#RUN pip3 install -r requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
RUN python3 -m pip install -r /tmp/requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000
