import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

from services.database_service import DatabaseService


class ReportView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Reports")
        self.geometry("850x500")

        self.db = DatabaseService()
        self.current_report = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Reports", font=("Arial", 18, "bold")).pack(pady=10)

        btn = tk.Frame(self)
        btn.pack(pady=10)

        tk.Button(btn, text="Student Tuition Report", width=22, command=self.student_tuition_report).grid(row=0, column=0, padx=5)
        tk.Button(btn, text="Course Registration Report", width=24, command=self.course_registration_report).grid(row=0, column=1, padx=5)
        tk.Button(btn, text="Export CSV", width=15, command=self.export_csv).grid(row=0, column=2, padx=5)

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def set_columns(self, columns):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = columns

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

    def student_tuition_report(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                students.student_id,
                students.name,
                IFNULL(SUM(courses.tuition_fee), 0) AS total_tuition
            FROM students
            LEFT JOIN registrations ON students.student_id = registrations.student_id
            LEFT JOIN courses ON registrations.course_id = courses.course_id
            GROUP BY students.student_id, students.name
        """)

        rows = cursor.fetchall()
        conn.close()

        self.current_report = rows
        self.set_columns(("student_id", "student_name", "total_tuition"))

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def course_registration_report(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                courses.course_id,
                courses.course_name,
                COUNT(registrations.student_id) AS number_of_students
            FROM courses
            LEFT JOIN registrations ON courses.course_id = registrations.course_id
            GROUP BY courses.course_id, courses.course_name
        """)

        rows = cursor.fetchall()
        conn.close()

        self.current_report = rows
        self.set_columns(("course_id", "course_name", "number_of_students"))

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def export_csv(self):
        if not self.current_report:
            messagebox.showwarning("Warning", "Please choose a report first!")
            return

        if not os.path.exists("exports"):
            os.makedirs("exports")

        file_path = os.path.join("exports", "report.csv")

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.tree["columns"])
            writer.writerows(self.current_report)

        messagebox.showinfo("Success", "Report exported to exports/report.csv")