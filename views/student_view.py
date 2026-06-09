import tkinter as tk
from tkinter import ttk, messagebox

from models.student import Student
from services.student_service import StudentService


class StudentView(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Student Management")
        self.geometry("750x500")

        self.student_service = StudentService()

        self.create_widgets()
        self.load_students()

    def create_widgets(self):
        title = tk.Label(self, text="Student Management", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(form_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form_frame)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(form_frame)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Major").grid(row=3, column=0, padx=5, pady=5)
        self.entry_major = tk.Entry(form_frame)
        self.entry_major.grid(row=3, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Update", width=10, command=self.update_student).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete", width=10, command=self.delete_student).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Search", width=10, command=self.search_student).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Clear", width=10, command=self.clear_form).grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(
            self,
            columns=("student_id", "name", "email", "major"),
            show="headings"
        )

        self.tree.heading("student_id", text="Student ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("major", text="Major")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = self.student_service.get_all_students()

        for student in students:
            self.tree.insert("", tk.END, values=student)

    def add_student(self):
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()
        major = self.entry_major.get()

        if student_id == "" or name == "":
            messagebox.showwarning("Warning", "Student ID and Name are required!")
            return

        student = Student(student_id, name, email, major)

        result = self.student_service.add_student(student)

        if result:
            messagebox.showinfo("Success", "Student added successfully!")
            self.load_students()
            self.clear_form()
        else:
            messagebox.showerror("Error", "Cannot add student!")

    def update_student(self):
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()
        major = self.entry_major.get()

        if student_id == "":
            messagebox.showwarning("Warning", "Please select a student!")
            return

        student = Student(student_id, name, email, major)
        self.student_service.update_student(student)

        messagebox.showinfo("Success", "Student updated successfully!")
        self.load_students()
        self.clear_form()

    def delete_student(self):
        student_id = self.entry_id.get()

        if student_id == "":
            messagebox.showwarning("Warning", "Please select a student!")
            return

        self.student_service.delete_student(student_id)

        messagebox.showinfo("Success", "Student deleted successfully!")
        self.load_students()
        self.clear_form()

    def search_student(self):
        keyword = self.entry_name.get()

        for row in self.tree.get_children():
            self.tree.delete(row)

        students = self.student_service.search_student(keyword)

        for student in students:
            self.tree.insert("", tk.END, values=student)

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_major.delete(0, tk.END)
        self.load_students()

    def on_select(self, event):
        selected_item = self.tree.selection()

        if selected_item:
            values = self.tree.item(selected_item[0], "values")

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])

            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, values[1])

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, values[2])

            self.entry_major.delete(0, tk.END)
            self.entry_major.insert(0, values[3])