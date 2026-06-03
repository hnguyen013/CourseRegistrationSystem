import sqlite3
from services.database_service import DatabaseService


class CourseService:
    def __init__(self):
        self.db = DatabaseService()

    def add_course(self, course, course_type):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO courses
                (course_id, course_name, credits, tuition_fee, course_type)
                VALUES (?, ?, ?, ?, ?)
            """, (
                course.course_id,
                course.course_name,
                course.credits,
                course.tuition_fee,
                course_type
            ))

            conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Course ID already exists!")
            return False

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            conn.close()

    def get_all_courses(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def update_course(self, course):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE courses
            SET course_name = ?, credits = ?, tuition_fee = ?
            WHERE course_id = ?
        """, (
            course.course_name,
            course.credits,
            course.tuition_fee,
            course.course_id
        ))

        conn.commit()
        conn.close()

    def delete_course(self, course_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM courses
            WHERE course_id = ?
        """, (course_id,))

        conn.commit()
        conn.close()