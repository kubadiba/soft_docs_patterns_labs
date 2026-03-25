import csv
from models import Course
from interfaces import ICourseRepository

class CourseImportService:
    def __init__(self, repository: ICourseRepository):
        self.repository = repository

    def import_from_csv(self, file_path: str):
        courses_to_import = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                new_course = Course(
                    course_id=row['course_id'],
                    title=row['title'],
                    price=float(row['price'])
                )
                courses_to_import.append(new_course)
        
        self.repository.add_courses(courses_to_import)
        return len(courses_to_import)