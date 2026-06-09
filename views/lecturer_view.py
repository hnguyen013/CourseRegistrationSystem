import tkinter as tk
from tkinter import ttk, messagebox

from models.lecturer import Lecturer
from services.lecturer_service import LecturerService


class LecturerView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Lecturer Management")
        self.geometry("750x500")

        self.lecturer_service = LecturerService()

        self.create_widgets()
        self.load_lecturers()

    def create_widgets(self):
        tk.Label(self, text="Lecturer Management", font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Lecturer ID").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(form)
        self.entry_id.grid(row=0, column=1)

        tk.Label(form, text="Name").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form)
        self.entry_name.grid(row=1, column=1)

        tk.Label(form, text="Email").grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(form)
        self.entry_email.grid(row=2, column=1)

        tk.Label(form, text="Department").grid(row=3, column=0, padx=5, pady=5)
        self.entry_department = tk.Entry(form)
        self.entry_department.grid(row=3, column=1)

        btn = tk.Frame(self)
        btn.pack(pady=10)

        tk.Button(btn, text="Add", width=10, command=self.add_lecturer).grid(row=0, column=0, padx=5)
        tk.Button(btn, text="Update", width=10, command=self.update_lecturer).grid(row=0, column=1, padx=5)
        tk.Button(btn, text="Delete", width=10, command=self.delete_lecturer).grid(row=0, column=2, padx=5)
        tk.Button(btn, text="Clear", width=10, command=self.clear_form).grid(row=0, column=3, padx=5)

        self.tree = ttk.Treeview(
            self,
            columns=("lecturer_id", "name", "email", "department"),
            show="headings"
        )

        for col in ("lecturer_id", "name", "email", "department"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def load_lecturers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for lecturer in self.lecturer_service.get_all_lecturers():
            self.tree.insert("", tk.END, values=lecturer)

    def add_lecturer(self):
        lecturer = Lecturer(
            self.entry_id.get(),
            self.entry_name.get(),
            self.entry_email.get(),
            self.entry_department.get()
        )

        if lecturer.person_id == "" or lecturer.name == "":
            messagebox.showwarning("Warning", "Lecturer ID and Name are required!")
            return

        if self.lecturer_service.add_lecturer(lecturer):
            messagebox.showinfo("Success", "Lecturer added!")
            self.load_lecturers()
            self.clear_form()
        else:
            messagebox.showerror("Error", "Cannot add lecturer!")

    def update_lecturer(self):
        lecturer = Lecturer(
            self.entry_id.get(),
            self.entry_name.get(),
            self.entry_email.get(),
            self.entry_department.get()
        )

        self.lecturer_service.update_lecturer(lecturer)
        messagebox.showinfo("Success", "Lecturer updated!")
        self.load_lecturers()
        self.clear_form()

    def delete_lecturer(self):
        lecturer_id = self.entry_id.get()

        if lecturer_id == "":
            messagebox.showwarning("Warning", "Please select lecturer!")
            return

        self.lecturer_service.delete_lecturer(lecturer_id)
        messagebox.showinfo("Success", "Lecturer deleted!")
        self.load_lecturers()
        self.clear_form()

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_department.delete(0, tk.END)

    def on_select(self, event):
        selected = self.tree.selection()

        if selected:
            values = self.tree.item(selected[0], "values")

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])

            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, values[1])

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, values[2])

            self.entry_department.delete(0, tk.END)
            self.entry_department.insert(0, values[3])