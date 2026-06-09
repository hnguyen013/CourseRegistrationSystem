import tkinter as tk

from views.student_view import StudentView
from views.lecturer_view import LecturerView
from views.course_view import CourseView
from views.registration_view import RegistrationView
from views.report_view import ReportView


class DashboardView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Course Registration System")
        self.geometry("400x430")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self,
            text="Course Registration System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=30)

        tk.Button(
            self,
            text="Student Management",
            width=25,
            height=2,
            command=self.open_student_view
        ).pack(pady=8)

        tk.Button(
            self,
            text="Lecturer Management",
            width=25,
            height=2,
            command=self.open_lecturer_view
        ).pack(pady=8)

        tk.Button(
            self,
            text="Course Management",
            width=25,
            height=2,
            command=self.open_course_view
        ).pack(pady=8)

        tk.Button(
            self,
            text="Course Registration",
            width=25,
            height=2,
            command=self.open_registration_view
        ).pack(pady=8)

        tk.Button(
            self,
            text="Reports",
            width=25,
            height=2,
            command=self.open_report_view
        ).pack(pady=8)

        tk.Button(
            self,
            text="Exit",
            width=25,
            height=2,
            command=self.destroy
        ).pack(pady=8)

    def open_student_view(self):
        StudentView()

    def open_lecturer_view(self):
        LecturerView()

    def open_course_view(self):
        CourseView()

    def open_registration_view(self):
        RegistrationView()

    def open_report_view(self):
        ReportView()