from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_id, course_name, credits, tuition_fee):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.tuition_fee = tuition_fee

    @abstractmethod
    def get_course_type(self):
        pass