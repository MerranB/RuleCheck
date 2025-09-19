from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck_ok():
    response = client.get("rulecheck/healthcheck")
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "ok"
    assert "environment" in body
    assert "version" in body
