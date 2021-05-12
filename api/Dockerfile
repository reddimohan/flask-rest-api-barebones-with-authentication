FROM python:3.7

# set working directory
WORKDIR /api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents writing pyc files to disc
ENV PYTHONUNBUFFERED 1 # Prevents Python from buffering stdout and stderr

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN pip install gunicorn
EXPOSE 5000

CMD [ "gunicorn", "app.ini"]
