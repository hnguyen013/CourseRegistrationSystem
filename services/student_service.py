import sqlite3
from services.database_service import DatabaseService


class StudentService:
    def __init__(self):
        self.db = DatabaseService()

    def add_student(self, student):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO students (student_id, name, email, major)
                VALUES (?, ?, ?, ?)
            """, (student.person_id, student.name, student.email, student.major))

            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Student ID already exists!")
            return False
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            conn.close()

    def get_all_students(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def update_student(self, student):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students
            SET name = ?, email = ?, major = ?
            WHERE student_id = ?
        """, (student.name, student.email, student.major, student.person_id))

        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))

        conn.commit()
        conn.close()

    def search_student(self, keyword):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM students
            WHERE student_id LIKE ? OR name LIKE ? OR major LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

        rows = cursor.fetchall()
        conn.close()
        return rows