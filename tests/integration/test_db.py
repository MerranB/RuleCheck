import pytest
from sqlalchemy import text


@pytest.mark.integration
def test_db_connection(db_session):
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1
