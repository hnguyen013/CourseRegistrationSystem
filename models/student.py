from models.person import Person

class Student(Person):
    def __init__(self, student_id, name, email, major):
        super().__init__(student_id, name, email)
        self.__major = major

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value