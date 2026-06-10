from models.person import Person

class Lecturer(Person):
    def __init__(self, lecturer_id, name, email, department):
        super().__init__(lecturer_id, name, email)
        self.__department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value