import os
from deepface import DeepFace
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from src.api.v1.models.employee_auth_model.employee_auth import EmployeeImage
from src.api.v1.repositories import api_employee_attendance_repository as _ATR
from src.api.v1.repositories import api_employee_auth_repository as _AR
from tempfile import NamedTemporaryFile
from config.config import settings
import pandas as pd
from src.api.v1.services import employee_detect_services as _EDS

router = APIRouter(prefix="/employee-detection")

@router.post("/upload_image")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # Create a temporary file to store the uploaded image
    try:
        with NamedTemporaryFile(delete=False, mode="wb") as temp_file:
            # Write the content of the uploaded file to the temporary file
            temp_file.write(await file.read())
            temp_file_path = temp_file.name

        # Now you have a valid path to pass into DeepFace
        # result = DeepFace.verify(
        #     img1_path=employee.image_path,
        #     img2_path="./1_dhvanil.jpg",
        #     model_name="VGG-Face",
        # )
        # result = DeepFace.verify(
        #     img1_path="./1_dhvanil.jpg",
        #     img2_path=employee.image_path
        # )
        # return {"message": "Image verification successful", "result": result}

        print(f'''{settings.UPLOAD_FOLDER=}''')
        print(f'''{temp_file_path=}''')
        result = DeepFace.find(
            img_path=temp_file_path,
            db_path=settings.UPLOAD_FOLDER,
            model_name="Facenet512"
        )
        print(f"DeepFace result: {result}")

        final_result = []
        for df in result:
            if isinstance(df, pd.DataFrame):
                # Convert DataFrame to list of dictionaries
                df = df.to_dict(orient="records")
                final_result.extend(df)
        
        employee_id = _EDS.check_employee_id(final_result)
        print(f'''{employee_id=}''')
        
        if employee_id is None:
            raise HTTPException(status_code=400, detail="Employee not found")

        await _ATR.create_attendance_record(employee_id, db)

        return {"message": "Image verification successful", "result": final_result}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup the temporary file after processing
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)