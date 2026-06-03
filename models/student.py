from models.person import Person

class Student(Person):
    def __init__(self, student_id, name, email, major):
        super().__init__(student_id, name, email)
        self.major = major