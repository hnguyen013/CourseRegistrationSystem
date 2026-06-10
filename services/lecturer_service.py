import sqlite3
from services.database_service import DatabaseService


class LecturerService:
    def __init__(self):
        self.db = DatabaseService()

    def add_lecturer(self, lecturer):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO lecturers (lecturer_id, name, email, department)
                VALUES (?, ?, ?, ?)
            """, (
                lecturer.person_id,
                lecturer.name,
                lecturer.email,
                lecturer.department
            ))

            conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Lecturer ID already exists!")
            return False

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            conn.close()

    def get_all_lecturers(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM lecturers")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def update_lecturer(self, lecturer):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE lecturers
            SET name = ?, email = ?, department = ?
            WHERE lecturer_id = ?
        """, (
            lecturer.name,
            lecturer.email,
            lecturer.department,
            lecturer.person_id
        ))

        conn.commit()
        conn.close()

    def delete_lecturer(self, lecturer_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM lecturers
            WHERE lecturer_id = ?
        """, (lecturer_id,))

        conn.commit()
        conn.close()
    def sort_lecturers(self, sort_by):
        conn = self.db.connect()
        cursor = conn.cursor()

        if sort_by == "id":
            cursor.execute("SELECT * FROM lecturers ORDER BY lecturer_id ASC")
        elif sort_by == "name":
            cursor.execute("SELECT * FROM lecturers ORDER BY name ASC")
        else:
            cursor.execute("SELECT * FROM lecturers")

        rows = cursor.fetchall()
        conn.close()
        return rows