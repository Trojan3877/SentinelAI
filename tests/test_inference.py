def test_inference_success(client):
    headers = {"Authorization": "Bearer test-key"}
    payload = {"prompt": "Explain AI in one sentence."}

    response = client.post("/infer", json=payload, headers=headers)

    assert response.status_code == 200
    assert "response" in response.json()
