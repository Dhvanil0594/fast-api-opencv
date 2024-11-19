from database.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)   
    position = Column(String(50), nullable=False)
    password = Column(String(255))
    images = relationship("EmployeeImage", back_populates="employee")
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    modified_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))

class EmployeeImage(Base):
    __tablename__ = 'employee_images'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    image_path = Column(String(100), nullable=False)
    employee = relationship("Employee", back_populates="images")
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    modified_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    