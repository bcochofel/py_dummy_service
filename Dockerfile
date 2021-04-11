FROM python:3.8-alpine
LABEL maintainer="Bruno Cochofel <bruno.cochofel@gmail.com>"

RUN apk update && apk add --no-cache \
    git \
    gcc \
    bash \
    openssh \
    musl-dev  \
    python3 \
    python3-dev \
    libxml2-dev  \
    libxslt-dev \
    linux-headers \
    expat \
    expat-dev \
    g++ \
    libstdc++ \
    make \
    swig

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENV WORKERS=2
ENV HOST="0.0.0.0"
ENV PORT=8080

COPY . /app
WORKDIR /app

RUN addgroup -g 5000 -S dummy && adduser -S dummy -u 5000 -G dummy

USER dummy

CMD [ "sh", "-c", "gunicorn -w ${WORKERS} \"py_dummy_service:create_app()\" -b \"${HOST}:${PORT}\""]
