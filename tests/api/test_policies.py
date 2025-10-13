import pytest


@pytest.mark.integration
def test_policy_endpoint(client):
    response = client.get("/rulecheck/policies/")
    assert response.status_code == 200
    assert "Policies endpoint ready" in response.json()["message"]


@pytest.mark.integration
def test_get_invalid_id(client):
    response = client.get(
        "/rulecheck/policies/get_policy/1000",
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Policy with ID 1000 not found"


@pytest.mark.integration
def test_create_and_get_policy(client):
    response = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response.json()
    policy_id = str(data["id"])
    assert response.status_code == 200

    response_get_call = client.get("/rulecheck/policies/get_policy/" + str(policy_id))
    data = response_get_call.json()
    assert response_get_call.status_code == 200
    assert data["title"] == "Travel Policy"


@pytest.mark.integration
def test_create_invalid_date_policy(client):
    response = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025/09/11T14:30:00Z",
        },
    )
    data = response.json()
    assert (
        data["detail"][0]["msg"]
        == "Input should be a valid datetime or date, invalid date separator, expected `-`"
    )
    assert response.status_code == 422


@pytest.mark.integration
def test_create_and_delete_policy(client):
    response_create = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response_create.json()
    policy_id = str(data["id"])
    assert response_create.status_code == 200

    response_delete = client.delete(
        "/rulecheck/policies/delete_policy/" + str(policy_id)
    )

    data = response_delete.json()
    assert response_delete.status_code == 200
    assert data["message"] == "Policy with ID " + policy_id + " deleted successfully"


@pytest.mark.integration
def test_delete_policy_invalid_id(client):
    response_delete = client.delete("/rulecheck/policies/delete_policy/1000")

    data = response_delete.json()
    assert response_delete.status_code == 404
    assert data["detail"] == "Policy with ID 1000 not found"


@pytest.mark.integration
def test_delete_policy_with_rules_attached(client):
    response = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )
    data = response.json()
    policy_id = str(data["id"])
    assert response.status_code == 200

    response_create_rule = client.post(
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
    assert response_create_rule.status_code == 200

    response_delete = client.delete(
        "/rulecheck/policies/delete_policy/" + str(policy_id)
    )

    data = response_delete.json()
    assert response_delete.status_code == 409
    assert (
        data["detail"]
        == "Please remove all rules from the Policy before deleting the policy"
    )


@pytest.mark.integration
def test_edit_policy(client):
    response = client.post(
        "/rulecheck/policies/create_policy",
        json={
            "title": "Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )

    data = response.json()
    policy_id = str(data["id"])
    assert response.status_code == 200

    response_update = client.put(
        "/rulecheck/policies/edit_policy/" + str(policy_id),
        json={
            "title": "The Travel Policy",
            "description": "Policy for the reimbursement of travel expensive",
            "version": "1.0.0",
            "effective_date": "2025-09-11T14:30:00Z",
        },
    )

    data = response_update.json()
    assert response_update.status_code == 200
    assert data["message"] == "Policy updated successfully"
