import pytest


@pytest.mark.integration
def test_create_and_get_action_submission(client):
    create_resp = client.post(
        "/rulecheck/action_submissions/create_action_submission",
        json={
            "user_id": "Jane Doe",
            "action_type": "reimbursement",
            "amount": 500.00,
            "expense_category": "meals",
            "purchase_type": "dinner",
            "vendor": "Olive Garden",
            "purchase_date": "2025-09-12T19:00:00Z",
            "location": "Houston, TX",
            "detail": "Team dinner during conference.",
        },
    )
    data = create_resp.json()
    submission_id = str(data["id"])
    assert create_resp.status_code == 200

    response = client.get(
        "/rulecheck/action_submissions/get_action_submission/" + submission_id,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["purchase_type"] == "dinner"


@pytest.mark.integration
def test_get_invalid_id(client):
    response = client.get(
        "/rulecheck/action_submissions/get_action_submission/1000",
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Action Submission with ID 1000 not found"


@pytest.mark.integration
def test_missing_type_create_action_submission(client):
    response = client.post(
        "/rulecheck/action_submissions/create_action_submission",
        json={
            "action_type": "reimbursement",
            "amount": 500.00,
            "expense_category": "meals",
            "purchase_type": "dinner",
            "vendor": "Olive Garden",
            "purchase_date": "2025-09-12T19:00:00Z",
            "location": "Houston, TX",
            "detail": "Team dinner during conference.",
        },
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["type"] == "missing"


@pytest.mark.integration
def test_wrong_type_create_action_submission(client):
    response = client.post(
        "/rulecheck/action_submissions/create_action_submission",
        json={
            "user_id": "Joe Smoe",
            "action_type": 7,
            "amount": 500.00,
            "expense_category": "meals",
            "purchase_type": "dinner",
            "vendor": "Olive Garden",
            "purchase_date": "2025-09-12T19:00:00Z",
            "location": "Houston, TX",
            "detail": "Team dinner during conference.",
        },
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["msg"] == "Input should be a valid string"
