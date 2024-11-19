from datetime import datetime,timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from database.database import Base

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))