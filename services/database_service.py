import sqlite3
import os


class DatabaseService:
    def __init__(self):
        self.db_path = os.path.join("database", "course_registration.db")

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT,
                major TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lecturers (
                lecturer_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT,
                department TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                credits INTEGER NOT NULL,
                tuition_fee REAL NOT NULL,
                course_type TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                course_id TEXT NOT NULL,
                registration_date TEXT,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        """)

        conn.commit()
        conn.close()