FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_APP=py_dummy_service
ENV FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
