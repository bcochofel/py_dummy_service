FROM python:3.8-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV WORKERS=2
ENV HOST="0.0.0.0"
ENV PORT=8080

COPY . /app
WORKDIR /app

RUN addgroup -g 5000 -S dummy && adduser -S dummy -u 5000 -G dummy

USER dummy

CMD [ "sh", "-c", "gunicorn -w ${WORKERS} \"py_dummy_service:create_app()\" -b \"${HOST}:${PORT}\""]
