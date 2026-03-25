from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base
from repositories import SQLAlchemyCourseRepository
from services import CourseImportService

# 1. Database Setup
engine = create_engine('sqlite:///edx_platform.db')
session_factory = scoped_session(sessionmaker(bind=engine))

# 2. Manual Dependency Injection Container
class IoCContainer:
    def __init__(self):
        # Injecting session_factory into Repository
        self.repo = SQLAlchemyCourseRepository(session_factory=session_factory)
        # Injecting Repository into Service
        self.import_service = CourseImportService(repository=self.repo)

if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(engine)
    
    # Initialize Container
    container = IoCContainer()
    service = container.import_service
    
    print("--- Starting Data Import Process ---")
    try:
        total = service.import_from_csv("data.csv")
        print(f"Success! Total courses added: {total}")
    except FileNotFoundError:
        print("Error: data.csv not found. Run 'python generator.py' first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")