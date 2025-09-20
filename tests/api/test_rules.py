import pytest


@pytest.mark.integration
def test_rule_endpoint(client):
    response = client.get("/rulecheck/rules/")
    assert response.status_code == 200
    assert "Rules endpoint ready" in response.json()["message"]
