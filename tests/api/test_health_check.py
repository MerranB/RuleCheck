def test_healthcheck(client):
    response = client.get("/rulecheck/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
