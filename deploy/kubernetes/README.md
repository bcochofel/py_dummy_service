# py-dummy-service

You can deploy both `frontend` and `backend` using the helm charts.

Add the helm chart repository:

```bash
helm repo add py-dummy-service https://bcochofel.github.io/py_dummy_service
```

Install the backend service:

```bash
helm upgrade -i backend py-dummy-service/py-dummy-service
```

Install lthe frontend service with the backend option:

```bash
helm upgrade -i frontend --set backend="http://backend-py-dummy-service" py-dummy-service/py-dummy-service
```
