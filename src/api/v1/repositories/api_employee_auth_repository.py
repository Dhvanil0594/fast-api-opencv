from fastapi import HTTPException, status
from src.api.v1.models.employee_auth_model.employee_auth import Employee, EmployeeImage
from logger import logger
from sqlalchemy.orm import Session


async def get_employee_by_email(email: str, db: Session):
    logger.info("Retrieving employee by email: %s", email)

    existing_employee = db.query(Employee).filter(Employee.email == email).first()
    if existing_employee:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    return existing_employee

async def get_employee_by_id(id: int, db: Session):
    logger.info("Retrieving employee by ID: %s", id)
    employee = db.query(Employee).filter(Employee.id == id).first()
    return employee

async def get_employee_image_by_id(id: int, db: Session):
    logger.info("Retrieving employee image by ID: %s", id)
    employee_image = db.query(EmployeeImage).filter(EmployeeImage.id == id).first()
    return employee_image

async def save_employee(employee: Employee, db: Session):
    logger.info("Saving employee: %s", employee)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


async def save_image(employee_image: EmployeeImage, db: Session):
    logger.info("Saving employee image")
    db.add(employee_image)
    db.commit()
    db.refresh(employee_image)
    return employee_image