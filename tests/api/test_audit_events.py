import pytest

from app.db.models import ActionSubmission, Decision
from app.db.models.audit_event import AuditEvent


@pytest.mark.integration
def test_get_audit_event(client, db_session):
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
        submission_id=new_action_submission.id,
        decision_type="allowed",
        explanation="Yap yap",
        matched_rule_ids=[1],
    )

    db_session.add(new_decision)
    db_session.commit()
    new_decision_id = new_decision.id

    new_audit = AuditEvent(
        submission_id=new_action_submission.id,
        decision_id=new_decision.id,
        actor_role="admin",
        action_type="approve",
    )
    db_session.add(new_audit)
    db_session.commit()

    # Step 2: Call your GET endpoint (replace with your route)
    response = client.get(
        "/rulecheck/audit_events/get_audit_event/" + str(new_audit.id)
    )

    # Step 3: Validate response
    assert response.status_code == 200
    data = response.json()
    assert data["actor_role"] == "admin"
    assert data["action_type"] == "approve"
    assert data["submission_id"] == new_action_submission_id
    assert data["decision_id"] == new_decision_id


@pytest.mark.integration
def test_get_invalid_id(client):
    response = client.get(
        "/rulecheck/audit_events/get_audit_event/1000",
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Audit Event with ID 1000 not found"
