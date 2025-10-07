import pytest

from app.db.models import Decision, ActionSubmission


@pytest.mark.integration
def test_get_decision(client, db_session):
    new_action_submission = ActionSubmission(
        amount=100,
        detail="test",
        expense_category="flight",
        location="Houston",
        purchase_date="2025-09-11T14:30:00Z",
        purchase_type="flight",
        user_id="Joe Smoe",
        vendor="Delta",
    )

    db_session.add(new_action_submission)
    db_session.commit()
    new_action_submission_id = new_action_submission.id

    new_decision = Decision(
        submission_id=new_action_submission_id,
        decision_type="allowed",
        explanation="Yap yap",
        matched_rule_ids=[1],
    )

    db_session.add(new_decision)
    db_session.commit()

    response = client.get("/rulecheck/decisions/get_decision/" + str(new_decision.id))
    assert response.status_code == 200
    data = response.json()
    assert data["decision_type"] == "allowed"


@pytest.mark.integration
def test_get_invalid_id(client):
    response = client.get(
        "/rulecheck/decisions/get_decision/1000",
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Decision with ID 1000 not found"
