# py_dummy_service

Python Flask Dummy Service

## Install requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

## Run locally

```bash
export FLASK_ENV=development
export FLASK_APP=py_dummy_service
flask run
```

valid values for env:

* development
* testing
* production (default)

you can check available routes using:

```bash
export FLASK_APP=py_dummy_service
flask routes
```

## Run tests and code coverage

```bash
make test
make report
```

## Run on Docker

```bash
make build
make run
make kill
```
