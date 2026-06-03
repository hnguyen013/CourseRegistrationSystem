from services.database_service import DatabaseService
from datetime import datetime


class RegistrationService:
    def __init__(self):
        self.db = DatabaseService()

    def register_course(self, student_id, course_id):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Check student exists
            cursor.execute(
                "SELECT * FROM students WHERE student_id = ?",
                (student_id,)
            )
            student = cursor.fetchone()

            if student is None:
                print("Student does not exist!")
                return False

            # Check course exists
            cursor.execute(
                "SELECT * FROM courses WHERE course_id = ?",
                (course_id,)
            )
            course = cursor.fetchone()

            if course is None:
                print("Course does not exist!")
                return False

            # Check duplicate registration
            cursor.execute("""
                SELECT * FROM registrations
                WHERE student_id = ? AND course_id = ?
            """, (student_id, course_id))

            existing = cursor.fetchone()

            if existing is not None:
                print("This student already registered this course!")
                return False

            registration_date = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO registrations
                (student_id, course_id, registration_date)
                VALUES (?, ?, ?)
            """, (student_id, course_id, registration_date))

            conn.commit()
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            conn.close()

    def get_all_registrations(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                registrations.registration_id,
                students.student_id,
                students.name,
                courses.course_id,
                courses.course_name,
                courses.credits,
                courses.tuition_fee,
                registrations.registration_date
            FROM registrations
            JOIN students ON registrations.student_id = students.student_id
            JOIN courses ON registrations.course_id = courses.course_id
        """)

        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_student_courses(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                courses.course_id,
                courses.course_name,
                courses.credits,
                courses.tuition_fee,
                registrations.registration_date
            FROM registrations
            JOIN courses ON registrations.course_id = courses.course_id
            WHERE registrations.student_id = ?
        """, (student_id,))

        rows = cursor.fetchall()
        conn.close()
        return rows

    def calculate_total_tuition(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT SUM(courses.tuition_fee)
            FROM registrations
            JOIN courses ON registrations.course_id = courses.course_id
            WHERE registrations.student_id = ?
        """, (student_id,))

        total = cursor.fetchone()[0]
        conn.close()

        if total is None:
            return 0

        return total

    def delete_registration(self, registration_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM registrations
            WHERE registration_id = ?
        """, (registration_id,))

        conn.commit()
        conn.close()