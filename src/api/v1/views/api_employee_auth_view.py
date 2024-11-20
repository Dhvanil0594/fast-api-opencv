import os
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from database.database import get_db
from src.api.v1.schemas import employee_schemas as _ES
from src.api.v1.models.employee_auth_model.employee_auth import Employee, EmployeeImage
from src.api.v1.services import auth_services as  _AS
from src.api.v1.repositories import api_employee_auth_repository as _AR
from config.config import settings
router = APIRouter(prefix="/employee-auth")

@router.post("/register", response_model=_ES.UserResponse)
async def register(employee: _ES.EmployeeCreate, db: Session = Depends(get_db)):
    if not employee.name or not employee.position or not employee.email:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="name, position and email are required")
    
    # check if already exists or not 
    await _AR.get_employee_by_email(employee.email, db)
    
    # hash the password
    hashed_password = await _AS.hash_password(employee.password)

    db_employee = Employee(name=employee.name, email=employee.email, position=employee.position, password=hashed_password)
    response = await _AR.save_employee(db_employee, db)
    return response

@router.post("/upload_image/{employee_id}")
async def upload_image(employee_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Ensure directory exists
    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
    
    # Check employee existence
    await _AR.get_employee_by_id(employee_id, db)
    
    # Save the uploaded image
    image_path = os.path.join(settings.UPLOAD_FOLDER, f"{employee_id}_{file.filename}")
    with open(image_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Store image path in the database
    await _AR.save_image(EmployeeImage(employee_id=employee_id, image_path=image_path), db)
    
    return {"message": "Image uploaded and face registered successfully"}