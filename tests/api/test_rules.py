import pytest


@pytest.mark.integration
def test_rule_endpoint(client):
    response = client.get("/rulecheck/rules/")
    assert response.status_code == 200
    assert "Rules endpoint ready" in response.json()["message"]


@pytest.mark.integration
def test_get_invalid_id(client):
    response = client.get(
        "/rulecheck/rules/get_rule/1000",
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Rule with ID 1000 not found"


@pytest.mark.integration
def test_create_rule(client):
    response_create_policy = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response_create_policy.json()
    policy_id = str(data["id"])
    assert response_create_policy.status_code == 200

    response_create = client.post(
        "/rulecheck/rules/create_rule",
        json={
            "policy_id": policy_id,
            "description": "Policy for the reimbursement of travel expenses",
            "field": "amount",
            "operator": "<=",
            "value": "1500",
            "expense_category": "flight",
            "action": "allow",
        },
    )
    assert response_create.status_code == 200
    data = response_create.json()
    assert data["message"] == "Rule created successfully"


@pytest.mark.integration
def test_create_rule_invalid_input(client):
    response_create_policy = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response_create_policy.json()
    policy_id = str(data["id"])
    assert response_create_policy.status_code == 200

    response_create = client.post(
        "/rulecheck/rules/create_rule",
        json={
            "policy_id": policy_id,
            "description": "Policy for the reimbursement of travel expenses",
            "field": "amount",
            "operator": "<=",
            "value": "1500",
            "expense_category": "flight",
            "action": 7,
        },
    )
    assert response_create.status_code == 422
    data = response_create.json()
    assert data["detail"][0]["msg"] == "Input should be a valid string"


@pytest.mark.integration
def test_create_rule_invalid_input_policy_id(client):
    response_create = client.post(
        "/rulecheck/rules/create_rule",
        json={
            "policy_id": 1000,
            "description": "Policy for the reimbursement of travel expenses",
            "field": "amount",
            "operator": "<=",
            "value": "1500",
            "expense_category": "flight",
            "action": "allow",
        },
    )
    assert response_create.status_code == 422
    data = response_create.json()
    assert data["detail"] == "Policy ID 1000 is invalid"


@pytest.mark.integration
def test_delete_rule(client):
    response_create_policy = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response_create_policy.json()
    policy_id = str(data["id"])
    assert response_create_policy.status_code == 200

    response_create = client.post(
        "/rulecheck/rules/create_rule",
        json={
            "policy_id": policy_id,
            "description": "Policy for the reimbursement of travel expenses",
            "field": "amount",
            "operator": "<=",
            "value": "1500",
            "expense_category": "flight",
            "action": "allow",
        },
    )
    assert response_create.status_code == 200
    data = response_create.json()
    rule_id = data["id"]
    assert data["message"] == "Rule created successfully"

    response_delete_rule = client.delete("/rulecheck/rules/delete_rule/" + str(rule_id))
    assert response_delete_rule.status_code == 200


@pytest.mark.integration
def test_delete_invalid_rule(client):
    response_create_policy = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response_create_policy.json()
    policy_id = str(data["id"])
    assert response_create_policy.status_code == 200

    response_create = client.post(
        "/rulecheck/rules/create_rule",
        json={
            "policy_id": policy_id,
            "description": "Policy for the reimbursement of travel expenses",
            "field": "amount",
            "operator": "<=",
            "value": "1500",
            "expense_category": "flight",
            "action": "allow",
        },
    )
    assert response_create.status_code == 200
    data = response_create.json()
    assert data["message"] == "Rule created successfully"

    response_delete_rule = client.delete("/rulecheck/rules/delete_rule/1000")
    assert response_delete_rule.status_code == 404
    data = response_delete_rule.json()
    assert data["detail"] == "Policy with ID 1000 not found"
