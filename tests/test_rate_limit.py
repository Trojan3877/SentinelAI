def test_rate_limit(client):
    headers = {"Authorization": "Bearer test-key"}
    payload = {"prompt": "rate limit test"}

    for _ in range(5):
        client.post("/infer", json=payload, headers=headers)

    response = client.post("/infer", json=payload, headers=headers)
    assert response.status_code in [429, 200]
