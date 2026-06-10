import tkinter as tk
from tkinter import ttk, messagebox

from models.student import Student
from services.student_service import StudentService
from views.style import COLORS, FONT_TITLE, FONT_NORMAL, FONT_BOLD, apply_style, make_button

# 1. IMPORT LỚP BASEVIEW TỪ FILE BASE_VIEW
from views.base_view import BaseView


# 2. SỬA ĐỂ LỚP STUDENTVIEW KẾ THỪA TỪ BASEVIEW
class StudentView(BaseView):
    def __init__(self):
        # 3. GỌI CONSTRUCTOR CỦA BASEVIEW VÀ TRUYỀN THAM SỐ YÊU CẦU
        # Tham số theo thứ tự: title, current_page, icon_text, subtitle
        super().__init__(
            title="Student Management",
            current_page="Student",
            icon_text="👨‍🎓",
            subtitle="Manage student information efficiently"
        )

        self.student_service = StudentService()

        # Tạo các widget chức năng riêng của trang Student và tải dữ liệu
        self.create_widgets()
        self.load_students()

    def create_widgets(self):
        # KHÔNG tạo lại container, sidebar, header nữa vì BaseView đã tạo sẵn rồi.
        # Ta vẽ trực tiếp các khối giao diện (Form, Bảng) vào vùng chứa `self.content` của BaseView.

        # --- Khối nhập thông tin sinh viên (Form Card) ---
        form_card = tk.LabelFrame(
            self.content,  # Sử dụng self.content kế thừa từ BaseView
            text="   👤 Student Information   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=25,
            pady=20
        )
        form_card.pack(fill="x", pady=(0, 16))

        self.entry_id = self.create_input(form_card, "Student ID", 0, 0, "Enter student id")
        self.entry_name = self.create_input(form_card, "Name", 0, 2, "Enter name")
        self.entry_email = self.create_input(form_card, "Email", 0, 4, "Enter email")
        self.entry_major = self.create_input(form_card, "Major", 0, 6, "Enter major")

        button_frame = tk.Frame(form_card, bg=COLORS["white"])
        button_frame.grid(row=2, column=0, columnspan=8, sticky="ew", pady=(20, 0))

        make_button(button_frame, "+   Add", self.add_student, COLORS["success"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "✎   Update", self.update_student, COLORS["info"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "🗑   Delete", self.delete_student, COLORS["danger"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "🔍   Search", self.search_student, COLORS["warning"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "↻   Clear", self.clear_form, COLORS["gray"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        # --- Khối danh sách hiển thị sinh viên (List Card) ---
        list_card = tk.LabelFrame(
            self.content,  # Sử dụng self.content kế thừa từ BaseView
            text="   ▦ Student List   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=18,
            pady=16
        )
        list_card.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            list_card,
            columns=("student_id", "name", "email", "major"),
            show="headings"
        )

        self.tree.heading("student_id", text="Student ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("major", text="Major")

        self.tree.column("student_id", width=60, anchor="center")
        self.tree.column("name", width=280)
        self.tree.column("email", width=330)
        self.tree.column("major", width=250)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # --- Nhãn hiển thị tổng số lượng sinh viên ---
        self.lbl_total = tk.Label(
            self.content,  # Sử dụng self.content kế thừa từ BaseView
            text="👥   Total: 0 students",
            bg=COLORS["bg"],
            fg=COLORS["primary"],
            font=("Arial", 11, "bold")
        )
        self.lbl_total.pack(anchor="w", pady=10)

    def create_input(self, parent, label, row, col, placeholder):
        tk.Label(
            parent,
            text=label,
            bg=COLORS["white"],
            fg=COLORS["text"],
            font=FONT_BOLD
        ).grid(row=row, column=col, sticky="w", padx=(0, 8), pady=6)

        entry = tk.Entry(
            parent,
            width=23,
            font=FONT_NORMAL,
            relief="solid",
            bd=1,
            fg=COLORS["muted"]
        )
        entry.grid(row=row + 1, column=col, columnspan=2, sticky="ew", padx=(0, 28), pady=6, ipady=7)
        entry.insert(0, placeholder)

        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg=COLORS["text"])

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg=COLORS["muted"])

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

        return entry

    def get_value(self, entry, placeholder):
        value = entry.get()
        return "" if value == placeholder else value

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = self.student_service.get_all_students()

        for student in students:
            self.tree.insert("", tk.END, values=student)

        self.lbl_total.config(text=f"👥   Total: {len(students)} students")

    def add_student(self):
        student_id = self.get_value(self.entry_id, "Enter student id")
        name = self.get_value(self.entry_name, "Enter name")
        email = self.get_value(self.entry_email, "Enter email")
        major = self.get_value(self.entry_major, "Enter major")

        if student_id == "" or name == "":
            messagebox.showwarning("Warning", "Student ID and Name are required!")
            return

        student = Student(student_id, name, email, major)

        if self.student_service.add_student(student):
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_form()
            self.load_students()
        else:
            messagebox.showerror("Error", "Cannot add student!")

    def update_student(self):
        student_id = self.get_value(self.entry_id, "Enter student id")
        name = self.get_value(self.entry_name, "Enter name")
        email = self.get_value(self.entry_email, "Enter email")
        major = self.get_value(self.entry_major, "Enter major")

        if student_id == "":
            messagebox.showwarning("Warning", "Please select a student!")
            return

        student = Student(student_id, name, email, major)
        self.student_service.update_student(student)

        messagebox.showinfo("Success", "Student updated successfully!")
        self.clear_form()
        self.load_students()

    def delete_student(self):
        student_id = self.get_value(self.entry_id, "Enter student id")

        if student_id == "":
            messagebox.showwarning("Warning", "Please select a student!")
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            return

        self.student_service.delete_student(student_id)
        messagebox.showinfo("Success", "Student deleted successfully!")
        self.clear_form()
        self.load_students()

    def search_student(self):
        keyword = self.get_value(self.entry_name, "Enter name")

        for row in self.tree.get_children():
            self.tree.delete(row)

        students = self.student_service.search_student(keyword)

        for student in students:
            self.tree.insert("", tk.END, values=student)

        self.lbl_total.config(text=f"👥   Search result: {len(students)} students")

    def clear_entry(self, entry, placeholder):
        entry.delete(0, tk.END)
        entry.insert(0, placeholder)
        entry.config(fg=COLORS["muted"])

    def clear_form(self):
        self.clear_entry(self.entry_id, "Enter student id")
        self.clear_entry(self.entry_name, "Enter name")
        self.clear_entry(self.entry_email, "Enter email")
        self.clear_entry(self.entry_major, "Enter major")
        self.load_students()

    def on_select(self, event):
        selected_item = self.tree.selection()

        if selected_item:
            values = self.tree.item(selected_item[0], "values")

            entries = [
                (self.entry_id, values[0]),
                (self.entry_name, values[1]),
                (self.entry_email, values[2]),
                (self.entry_major, values[3])
            ]

            for entry, value in entries:
                entry.delete(0, tk.END)
                entry.insert(0, value)
                entry.config(fg=COLORS["text"])