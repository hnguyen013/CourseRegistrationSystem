import tkinter as tk
from tkinter import ttk, messagebox

from services.student_service import StudentService
from services.course_service import CourseService
from services.registration_service import RegistrationService


class RegistrationView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Course Registration")
        self.geometry("850x500")

        self.student_service = StudentService()
        self.course_service = CourseService()
        self.registration_service = RegistrationService()

        self.students = []
        self.courses = []

        self.create_widgets()
        self.load_combobox_data()
        self.load_registrations()

    def create_widgets(self):
        tk.Label(self, text="Course Registration", font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Student").grid(row=0, column=0, padx=5, pady=5)
        self.cbo_student = ttk.Combobox(form, width=35, state="readonly")
        self.cbo_student.grid(row=0, column=1, padx=5)

        tk.Label(form, text="Course").grid(row=1, column=0, padx=5, pady=5)
        self.cbo_course = ttk.Combobox(form, width=35, state="readonly")
        self.cbo_course.grid(row=1, column=1, padx=5)

        tk.Button(form, text="Register", width=15, command=self.register_course).grid(row=2, column=1, pady=10)

        self.lbl_total = tk.Label(self, text="Total Tuition: 0", font=("Arial", 12, "bold"))
        self.lbl_total.pack(pady=5)

        self.tree = ttk.Treeview(
            self,
            columns=("registration_id", "student_id", "student_name", "course_id", "course_name", "credits", "fee", "date"),
            show="headings"
        )

        for col in ("registration_id", "student_id", "student_name", "course_id", "course_name", "credits", "fee", "date"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def load_combobox_data(self):
        self.students = self.student_service.get_all_students()
        self.courses = self.course_service.get_all_courses()

        self.cbo_student["values"] = [
            f"{s[0]} - {s[1]}" for s in self.students
        ]

        self.cbo_course["values"] = [
            f"{c[0]} - {c[1]}" for c in self.courses
        ]

    def register_course(self):
        if self.cbo_student.get() == "" or self.cbo_course.get() == "":
            messagebox.showwarning("Warning", "Please select student and course!")
            return

        student_id = self.cbo_student.get().split(" - ")[0]
        course_id = self.cbo_course.get().split(" - ")[0]

        result = self.registration_service.register_course(student_id, course_id)

        if result:
            messagebox.showinfo("Success", "Course registered successfully!")
            self.load_registrations()
            total = self.registration_service.calculate_total_tuition(student_id)
            self.lbl_total.config(text=f"Total Tuition: {total}")
        else:
            messagebox.showerror("Error", "Cannot register course!")

    def load_registrations(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for reg in self.registration_service.get_all_registrations():
            self.tree.insert("", tk.END, values=reg)