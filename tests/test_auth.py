def test_missing_api_key(client):
    response = client.post("/infer", json={"prompt": "Hello"})
    assert response.status_code == 401
