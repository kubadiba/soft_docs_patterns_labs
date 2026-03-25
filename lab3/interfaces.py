from abc import ABC, abstractmethod

class ICourseRepository(ABC):
    @abstractmethod
    def add_courses(self, courses):
        pass

class IPresentation(ABC):
    @abstractmethod
    def show_message(self, message: str):
        pass