# FastAPI Employee Register

A FastAPI project managing an **in-memory register of employees**.

## Features
- Add a new employee (first name, last name, email)
- List all employees
- Remove an employee by email
- Environment-based settings, ready for Docker & Compose

## Quickstart

```bash
# 1) Create virtualenv and install deps
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# 2) Copy env
cp .env.example .env

# 3) Run API
uvicorn employee_api.main:app --reload --port ${PORT:-8000}
```

## Endpoints
| Method | Path | Description |
|---------|------|-------------|
| GET | `/api/employees/` | List all employees |
| POST | `/api/employees/` | Add new employee |
| DELETE | `/api/employees/{email}` | Remove employee by email |

## Docker

```bash
docker build -t fastapi-employee:latest .
docker run --env-file .env -p 8000:8000 fastapi-employee:latest
```
or
```bash
docker compose up --build
```

## Tests
```bash
pytest -q
```

