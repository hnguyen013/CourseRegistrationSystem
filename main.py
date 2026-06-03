from services.database_service import DatabaseService
from services.student_service import StudentService
from services.course_service import CourseService
from services.registration_service import RegistrationService

from models.student import Student
from models.compulsory_course import CompulsoryCourse


db = DatabaseService()
db.create_tables()

student_service = StudentService()
course_service = CourseService()
registration_service = RegistrationService()

student1 = Student(
    "S002",
    "Tran Van B",
    "b@gmail.com",
    "Software Engineering"
)

course1 = CompulsoryCourse(
    "C001",
    "Python Programming",
    3,
    1500000
)

student_service.add_student(student1)
course_service.add_course(course1, "Compulsory")

registration_service.register_course("S002", "C001")

print("All registrations:")
for r in registration_service.get_all_registrations():
    print(r)

print("Student courses:")
for c in registration_service.get_student_courses("S002"):
    print(c)

print("Total tuition:")
print(registration_service.calculate_total_tuition("S002"))