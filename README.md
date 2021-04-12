# py_dummy_service

[![codecov](https://codecov.io/gh/bcochofel/py_dummy_service/branch/main/graph/badge.svg)](https://codecov.io/gh/bcochofel/py_dummy_service)
[![pre-commit badge][pre-commit-badge]][pre-commit] [![Conventional commits badge][conventional-commits-badge]][conventional-commits] [![Keep a Changelog v1.1.0 badge][keep-a-changelog-badge]][keep-a-changelog] [![MIT License Badge][license-badge]][license]

Python Flask Dummy Service

## Install requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

additional requirements for running tests

```bash
pip install black pytest coverage gunicorn
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

## Open Tracing

To send traces to Jaeger set the `JAEGER_HOST` environment variable.

## pre-commit hooks

Read the [pre-commit hooks](docs/pre-commit-hooks.md) document for more info.

## git-chglog

Read the [git-chglog](docs/git-chlog.md) document for more info.

[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[conventional-commits-badge]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-green.svg
[conventional-commits]: https://conventionalcommits.org
[keep-a-changelog-badge]: https://img.shields.io/badge/changelog-Keep%20a%20Changelog%20v1.1.0-%23E05735
[keep-a-changelog]: https://keepachangelog.com/en/1.0.0/
[license]: ./LICENSE
[license-badge]: https://img.shields.io/badge/license-MIT-green.svg
[changelog]: ./CHANGELOG.md
[changelog-badge]: https://img.shields.io/badge/changelog-Keep%20a%20Changelog%20v1.1.0-%23E05735
