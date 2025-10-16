from fastapi import APIRouter, HTTPException

from employee_api.models.employee import Employee
from employee_api.services.employee_service import (
    add_employee,
    list_employees,
    remove_employee_by_email,
)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=list[Employee])
def get_employees():
    return list_employees()


@router.post("/", response_model=Employee, status_code=201)
def create_employee(emp: Employee):
    try:
        add_employee(emp)
    except ValueError as ex:
        raise HTTPException(status_code=409, detail=str(ex)) from ex
    return emp


@router.delete("/{email}", status_code=204)
def delete_employee(email: str):
    # email in path must be URL-encoded when calling (e.g. john.doe%40example.com)
    if not remove_employee_by_email(email):
        raise HTTPException(status_code=404, detail="Employee not found")
