FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV WORKERS=2
ENV HOST="0.0.0.0"
ENV PORT=8080

COPY . /app
WORKDIR /app

CMD [ "sh", "-c", "gunicorn -w ${WORKERS} \"py_dummy_service:create_app()\" -b \"${HOST}:${PORT}\""]
