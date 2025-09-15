# RuleCheck

RuleCheck is a FastAPI microservice designed for evaluating **rules**, **policies**, and **action submissions** to determine compliance outcomes.  
 
---

## Features

- FastAPI for building APIs
- SQLAlchemy for database models and persistence
- Alembic for migrations
- Pydantic for schemas and validation
- Docker + Docker Compose for local development
- Environment-specific settings
- Unit testing with pytest

---

## Project Layout

~~~
app/
├── api/             # API routers (controllers)
│   ├── __init__.py
│   ├── healthcheck.py
│   ├── action_submission.py
│   └── ...
│
├── core/            # Core config and settings
│   ├── __init__.py
│   └── config.py
│
├── db/              # Database logic
│   ├── __init__.py
│   ├── base.py
│   ├── database.py
│   └── model/
│       ├── __init__.py
│       ├── rule.py
│       ├── policy.py
│       ├── action_submission.py
│       └── decision.py
│
├── schemas/         # Pydantic schemas
│   ├── __init__.py
│   └── rule/
│       ├── create_rule.py
│       └── read_rule.py
│
├── tests/           # Pytest tests
│   └── test_rule.py
│
└── main.py          # FastAPI entrypoint

alembic/             # Alembic migrations
docker-compose.yml   # Local dev services
requirements.txt     # Python dependencies
.env.dev             # Local development environment
~~~

---

## Environment Configuration

 `.env.dev`:

~~~ini
DB_USER=<your-database-username>
DB_PASSWORD=<your-database-password>
DB_NAME=<your-database-name>
DB_HOST=localhost
DB_PORT=5432
~~~

---

## Running Locally

1. Start PostgreSQL using Docker:
   ~~~bash
   docker-compose up -d
   ~~~

2. Apply migrations:
   ~~~bash
   alembic upgrade head
   ~~~

3. Run the FastAPI app:
   ~~~bash
   uvicorn app.main:app --reload
   ~~~

4. Visit the API docs:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Testing

Run all tests with:

~~~bash
pytest
~~~

---
