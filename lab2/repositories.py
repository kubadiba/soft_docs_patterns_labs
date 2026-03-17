from interfaces import ICourseRepository

class SQLAlchemyCourseRepository(ICourseRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add_courses(self, courses):
        with self.session_factory() as session:
            session.add_all(courses)
            session.commit()
            print(f"DAL: Saved {len(courses)} records to database.")