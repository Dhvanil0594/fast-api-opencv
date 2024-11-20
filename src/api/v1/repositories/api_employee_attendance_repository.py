from src.api.v1.models.employee_attendance_model.employee_attendance import Attendance
from logger import logger
from sqlalchemy.orm import Session

async def create_attendance_record(employee_id: int, db: Session):
    logger.info("Creating attendance record for employee ID: %s", employee_id)
    attendance = Attendance(employee_id=employee_id)
    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance