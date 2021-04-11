FROM python:3.8-slim-buster
LABEL maintainer="Bruno Cochofel <bruno.cochofel@gmail.com>"

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENV WORKERS=2
ENV HOST="0.0.0.0"
ENV PORT=8080

COPY . /app
WORKDIR /app

RUN groupadd --gid 5000 --system dummy && useradd --system dummy --uid 5000 --gid dummy
USER dummy

CMD [ "sh", "-c", "gunicorn -w ${WORKERS} \"py_dummy_service:create_app()\" -b \"${HOST}:${PORT}\""]
