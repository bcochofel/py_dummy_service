def test_not_found(client):
    response = client.get("/notfound")
    assert response.status_code == 404