from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_id, course_name, credits, tuition_fee):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits
        self.__tuition_fee = tuition_fee

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, value):
        self.__course_id = value

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        self.__course_name = value

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        self.__credits = value

    @property
    def tuition_fee(self):
        return self.__tuition_fee

    @tuition_fee.setter
    def tuition_fee(self, value):
        self.__tuition_fee = value

    @abstractmethod
    def get_course_type(self):
        pass