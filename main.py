from models.student import Student
from models.lecturer import Lecturer
from models.compulsory_course import CompulsoryCourse
from models.elective_course import ElectiveCourse


# Create Student object
student1 = Student(
    "S001",
    "Nguyen Van A",
    "a@gmail.com",
    "Information Technology"
)

# Create Lecturer object
lecturer1 = Lecturer(
    "L001",
    "Tran Thi B",
    "b@gmail.com",
    "Computer Science"
)

# Create Course object
course1 = CompulsoryCourse(
    "C001",
    "Python Programming",
    3,
    1500000
)

course2 = ElectiveCourse(
    "C002",
    "Graphic Design",
    2,
    1000000
)

# Print data
print(student1.name)
print(lecturer1.department)
print(course1.course_name)
print(course2.tuition_fee)
from services.database_service import DatabaseService

db = DatabaseService()
db.create_tables()

print("Database and tables created successfully!")