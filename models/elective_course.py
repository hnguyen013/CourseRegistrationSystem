from models.course import Course

class ElectiveCourse(Course):
    def __init__(self, course_id, course_name, credits, tuition_fee):
        super().__init__(course_id, course_name, credits, tuition_fee)