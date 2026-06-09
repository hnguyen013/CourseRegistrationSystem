import tkinter as tk
from tkinter import ttk, messagebox

from models.compulsory_course import CompulsoryCourse
from models.elective_course import ElectiveCourse
from services.course_service import CourseService


class CourseView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Course Management")
        self.geometry("800x500")

        self.course_service = CourseService()
        self.course_type = tk.StringVar(value="Compulsory")

        self.create_widgets()
        self.load_courses()

    def create_widgets(self):
        tk.Label(self, text="Course Management", font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Course ID").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(form)
        self.entry_id.grid(row=0, column=1)

        tk.Label(form, text="Course Name").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form)
        self.entry_name.grid(row=1, column=1)

        tk.Label(form, text="Credits").grid(row=2, column=0, padx=5, pady=5)
        self.entry_credits = tk.Entry(form)
        self.entry_credits.grid(row=2, column=1)

        tk.Label(form, text="Tuition Fee").grid(row=3, column=0, padx=5, pady=5)
        self.entry_fee = tk.Entry(form)
        self.entry_fee.grid(row=3, column=1)

        tk.Label(form, text="Course Type").grid(row=4, column=0, padx=5, pady=5)
        tk.Radiobutton(form, text="Compulsory", variable=self.course_type, value="Compulsory").grid(row=4, column=1)
        tk.Radiobutton(form, text="Elective", variable=self.course_type, value="Elective").grid(row=4, column=2)

        btn = tk.Frame(self)
        btn.pack(pady=10)

        tk.Button(btn, text="Add", width=10, command=self.add_course).grid(row=0, column=0, padx=5)
        tk.Button(btn, text="Update", width=10, command=self.update_course).grid(row=0, column=1, padx=5)
        tk.Button(btn, text="Delete", width=10, command=self.delete_course).grid(row=0, column=2, padx=5)
        tk.Button(btn, text="Clear", width=10, command=self.clear_form).grid(row=0, column=3, padx=5)

        self.tree = ttk.Treeview(
            self,
            columns=("course_id", "course_name", "credits", "tuition_fee", "course_type"),
            show="headings"
        )

        for col in ("course_id", "course_name", "credits", "tuition_fee", "course_type"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def load_courses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for course in self.course_service.get_all_courses():
            self.tree.insert("", tk.END, values=course)

    def add_course(self):
        try:
            course_id = self.entry_id.get()
            name = self.entry_name.get()
            credits = int(self.entry_credits.get())
            fee = float(self.entry_fee.get())
            course_type = self.course_type.get()

            if course_id == "" or name == "":
                messagebox.showwarning("Warning", "Course ID and Name are required!")
                return

            if credits <= 0 or fee < 0:
                messagebox.showwarning("Warning", "Credits and tuition fee must be valid!")
                return

            if course_type == "Compulsory":
                course = CompulsoryCourse(course_id, name, credits, fee)
            else:
                course = ElectiveCourse(course_id, name, credits, fee)

            if self.course_service.add_course(course, course_type):
                messagebox.showinfo("Success", "Course added!")
                self.load_courses()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Cannot add course!")

        except ValueError:
            messagebox.showerror("Error", "Credits must be integer and fee must be number!")

    def update_course(self):
        try:
            course_id = self.entry_id.get()
            name = self.entry_name.get()
            credits = int(self.entry_credits.get())
            fee = float(self.entry_fee.get())

            course = CompulsoryCourse(course_id, name, credits, fee)
            self.course_service.update_course(course)

            messagebox.showinfo("Success", "Course updated!")
            self.load_courses()
            self.clear_form()

        except ValueError:
            messagebox.showerror("Error", "Invalid credits or tuition fee!")

    def delete_course(self):
        course_id = self.entry_id.get()

        if course_id == "":
            messagebox.showwarning("Warning", "Please select course!")
            return

        self.course_service.delete_course(course_id)
        messagebox.showinfo("Success", "Course deleted!")
        self.load_courses()
        self.clear_form()

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_credits.delete(0, tk.END)
        self.entry_fee.delete(0, tk.END)
        self.course_type.set("Compulsory")

    def on_select(self, event):
        selected = self.tree.selection()

        if selected:
            values = self.tree.item(selected[0], "values")

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])

            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, values[1])

            self.entry_credits.delete(0, tk.END)
            self.entry_credits.insert(0, values[2])

            self.entry_fee.delete(0, tk.END)
            self.entry_fee.insert(0, values[3])

            self.course_type.set(values[4])