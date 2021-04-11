def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200


def test_headers(client):
    response = client.get("/headers")
    assert response.status_code == 200
