import os
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status, Request
from sqlalchemy.orm import Session
from database.database import get_db
from src.api.v1.schemas import employee_schemas as _ES
from src.api.v1.models.employee_auth_model.employee_auth import Employee, EmployeeImage
from src.api.v1.services import auth_services as  _AS
from config.config import settings

router = APIRouter(prefix="/employee-auth")

@router.post("/register", response_model=_ES.UserResponse)
async def register(employee: _ES.EmployeeCreate, db: Session = Depends(get_db)):
    if not employee.name or not employee.position or not employee.email:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="name, position and email are required")
    
    # check if already exists or not 
    existing_user = db.query(Employee).filter(Employee.email == Employee.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # hash the password
    hashed_password = await _AS.hash_password(employee.password)

    db_employee = Employee(name=employee.name, email=employee.email, position=employee.position, password=hashed_password)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.post("/upload_image/{employee_id}")
async def upload_image(employee_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Ensure directory exists
    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
    
    # Check employee existence
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Save the uploaded image
    image_path = os.path.join(settings.UPLOAD_FOLDER, f"{employee_id}_{file.filename}")
    with open(image_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # # Load the image and detect the face
    # image = face_recognition.load_image_file(image_path)
    # face_encodings = face_recognition.face_encodings(image)
    
    # if not face_encodings:
    #     os.remove(image_path)
    #     raise HTTPException(status_code=400, detail="No face detected in the image")
    
    # # Store the face encoding in the database
    # face_encoding = face_encodings[0]
    # new_face = EmployeeFace(employee_id=employee_id, face_encoding=face_encoding)
    # db.add(new_face)
    # db.commit()
    
    # Store image path in the database
    new_image = EmployeeImage(employee_id=employee_id, image_path=image_path)
    db.add(new_image)
    db.commit()
    
    return {"message": "Image uploaded and face registered successfully"}