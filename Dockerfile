FROM python:3.7.1

LABEL Author="Patricia Bonaldy"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "backend/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0
