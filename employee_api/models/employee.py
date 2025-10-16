from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
