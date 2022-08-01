def test_headers(client):
    response = client.get("/api/v1/headers")
    assert response.status_code == 200


def test_status404(client):
    response = client.get("/api/v1/status/404")
    assert response.status_code == 404


def test_status503(client):
    response = client.get("/api/v1/status/503")
    assert response.status_code == 503


def test_path1(client):
    response = client.get("/api/v1/path1")
    assert response.status_code == 200


def test_path2(client):
    response = client.get("/api/v1/path2")
    assert response.status_code == 200
