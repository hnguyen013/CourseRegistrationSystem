from models.person import Person

class Lecturer(Person):
    def __init__(self, lecturer_id, name, email, department):
        super().__init__(lecturer_id, name, email)
        self.department = department