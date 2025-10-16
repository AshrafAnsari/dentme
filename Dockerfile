# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (optional, keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir --upgrade pip &&     pip install --no-cache-dir ".[dev]"

COPY employee_api ./employee_api

EXPOSE 8000
CMD ["uvicorn", "employee_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
