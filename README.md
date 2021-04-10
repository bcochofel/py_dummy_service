# py_dummy_service

Python Flask Dummy Service

## Docker build

```bash
docker build --tag py-dummy-service .
docker tag py-dummy-service:latest py-dummy-service:0.2.0
docker run --publish 8080:8080 py-dummy-service
```
