from employee_api.models.employee import Employee

_employees: list[Employee] = []


def list_employees() -> list[Employee]:
    return _employees


def add_employee(emp: Employee) -> None:
    # uniqueness on email only
    if any(e.email.lower() == emp.email.lower() for e in _employees):
        raise ValueError("Employee with this email already exists")
    _employees.append(emp)


def remove_employee_by_email(email: str) -> bool:
    idx = next((i for i, e in enumerate(_employees) if e.email.lower() == email.lower()), None)
    if idx is None:
        return False
    _employees.pop(idx)
    return True
