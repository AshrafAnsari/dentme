from urllib.parse import quote

from fastapi.testclient import TestClient

from employee_api.main import app

client = TestClient(app)


def test_employees_crud():
    # list empty
    r = client.get("/api/employees/")
    assert r.status_code == 200
    assert r.json() == []

    # create
    payload = {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}
    r = client.post("/api/employees/", json=payload)
    assert r.status_code == 201
    assert r.json()["email"] == payload["email"]
    assert r.json()["first_name"] == "John"

    # list has one
    r = client.get("/api/employees/")
    assert r.status_code == 200
    assert len(r.json()) == 1

    # conflict on duplicate email
    dup = {"first_name": "Same", "last_name": "Email", "email": "john.doe@example.com"}
    r = client.post("/api/employees/", json=dup)
    assert r.status_code == 409

    # create second employee
    payload2 = {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com"}
    r = client.post("/api/employees/", json=payload2)
    assert r.status_code == 201
    assert r.json()["email"] == payload2["email"]
    assert r.json()["first_name"] == "Jane"

    # list has two
    r = client.get("/api/employees/")
    assert r.status_code == 200
    assert len(r.json()) == 2

    # delete by email (URL-encoded)
    email = quote("john.doe@example.com", safe="")
    r = client.delete(f"/api/employees/{email}")
    assert r.status_code == 204

    # delete missing
    r = client.delete(f"/api/employees/{email}")
    assert r.status_code == 404
