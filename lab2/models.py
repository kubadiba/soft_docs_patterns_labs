from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    course_id = Column(String, unique=True)
    title = Column(String)
    price = Column(Float)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)  # 'student' or 'teacher'