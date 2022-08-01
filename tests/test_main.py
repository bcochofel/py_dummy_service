def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_info(client):
    response = client.get("/info")
    assert response.status_code == 200


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
