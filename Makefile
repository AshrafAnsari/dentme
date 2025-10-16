.PHONY: run dev test lint format type

dev:
	uvicorn employee_api.main:app --reload --port $${PORT:-8000}

up:
	docker compose up --build

test:
	pytest -q --cov=employee_api --cov-report=term-missing

lint:
	ruff check .

format:
	black .
	ruff check --fix .

type:
	mypy employee_api
