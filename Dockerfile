FROM python:3.10.5

WORKDIR /django-website

LABEL maintainer="Jose Geancarlo Bermudez Blandon"

copy . .

RUN python -m pip install -r requirements.txt

WORKDIR /django-website/studybud


CMD [ "python","manage.py","runserver" , "0.0.0.0:8000"]


