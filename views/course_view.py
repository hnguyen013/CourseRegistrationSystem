import tkinter as tk
from tkinter import ttk, messagebox

from models.compulsory_course import CompulsoryCourse
from models.elective_course import ElectiveCourse
from services.course_service import CourseService
from views.style import COLORS, FONT_NORMAL, FONT_BOLD, apply_style, make_button

# 1. IMPORT LỚP BASEVIEW TỪ FILE BASE_VIEW
from views.base_view import BaseView


# 2. SỬA ĐỂ LỚP COURSEVIEW KẾ THỪA TỪ BASEVIEW
class CourseView(BaseView):
    def __init__(self):
        # 3. GỌI CONSTRUCTOR CỦA BASEVIEW VÀ TRUYỀN THAM SỐ GIAO DIỆN
        # Tham số theo thứ tự: title, current_page, icon_text, subtitle
        super().__init__(
            title="Course Management",
            current_page="Course",
            icon_text="📚",
            subtitle="Manage compulsory and elective courses"
        )

        self.course_service = CourseService()
        self.course_type = tk.StringVar(value="Compulsory")

        # Khởi tạo phần giao diện đặc trưng và tải dữ liệu môn học
        self.create_widgets()
        self.load_courses()

    def create_widgets(self):
        # KHÔNG tạo lại container, sidebar, và header nữa vì BaseView đã quản lý.
        # Ta vẽ trực tiếp Form và Bảng dữ liệu vào vùng chứa `self.content` kế thừa từ BaseView.

        # --- Khối thông tin khóa học (Form Card) ---
        form_card = tk.LabelFrame(
            self.content,  # Đổi từ content thành self.content để dùng biến của lớp cha
            text="   📘 Course Information   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=25,
            pady=20
        )
        form_card.pack(fill="x", pady=(0, 16))

        self.entry_id = self.create_input(form_card, "Course ID", 0, 0, "Enter course id")
        self.entry_name = self.create_input(form_card, "Course Name", 0, 2, "Enter course name")
        self.entry_credits = self.create_input(form_card, "Credits", 0, 4, "Enter credits")
        self.entry_fee = self.create_input(form_card, "Tuition Fee", 0, 6, "Enter tuition fee")

        # --- Chọn loại môn học (Radio Buttons) ---
        type_frame = tk.Frame(form_card, bg=COLORS["white"])
        type_frame.grid(row=2, column=0, columnspan=4, sticky="w", pady=(20, 0))

        tk.Label(
            type_frame,
            text="Course Type:",
            bg=COLORS["white"],
            fg=COLORS["text"],
            font=FONT_BOLD
        ).pack(side="left", padx=(0, 15))

        tk.Radiobutton(
            type_frame,
            text="Compulsory",
            variable=self.course_type,
            value="Compulsory",
            bg=COLORS["white"],
            fg=COLORS["text"],
            selectcolor=COLORS["white"],
            activebackground=COLORS["white"],
            font=FONT_BOLD
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            type_frame,
            text="Elective",
            variable=self.course_type,
            value="Elective",
            bg=COLORS["white"],
            fg=COLORS["text"],
            selectcolor=COLORS["white"],
            activebackground=COLORS["white"],
            font=FONT_BOLD
        ).pack(side="left", padx=10)

        # --- Khối nút chức năng ---
        button_frame = tk.Frame(form_card, bg=COLORS["white"])
        button_frame.grid(row=3, column=0, columnspan=8, sticky="ew", pady=(20, 0))

        make_button(button_frame, "+   Add", self.add_course, COLORS["success"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "✎   Update", self.update_course, COLORS["info"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "🗑   Delete", self.delete_course, COLORS["danger"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "↻   Clear", self.clear_form, COLORS["gray"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        # --- Khối hiển thị danh sách môn học (List Card) ---
        list_card = tk.LabelFrame(
            self.content,  # Đổi từ content thành self.content
            text="   ▦ Course List   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=18,
            pady=16
        )
        list_card.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            list_card,
            columns=("course_id", "course_name", "credits", "tuition_fee", "course_type"),
            show="headings"
        )

        self.tree.heading("course_id", text="Course ID")
        self.tree.heading("course_name", text="Course Name")
        self.tree.heading("credits", text="Credits")
        self.tree.heading("tuition_fee", text="Tuition Fee")
        self.tree.heading("course_type", text="Course Type")

        self.tree.column("course_id", width=80, anchor="center")
        self.tree.column("course_name", width=330)
        self.tree.column("credits", width=100, anchor="center")
        self.tree.column("tuition_fee", width=180, anchor="center")
        self.tree.column("course_type", width=180, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # --- Nhãn tổng số khóa học ---
        self.lbl_total = tk.Label(
            self.content,  # Đổi từ content thành self.content
            text="📚   Total: 0 courses",
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

    def load_courses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        courses = self.course_service.get_all_courses()

        for course in courses:
            self.tree.insert("", tk.END, values=course)

        self.lbl_total.config(text=f"📚   Total: {len(courses)} courses")

    def add_course(self):
        try:
            course_id = self.get_value(self.entry_id, "Enter course id")
            name = self.get_value(self.entry_name, "Enter course name")
            credits_text = self.get_value(self.entry_credits, "Enter credits")
            fee_text = self.get_value(self.entry_fee, "Enter tuition fee")
            course_type = self.course_type.get()

            if course_id == "" or name == "":
                messagebox.showwarning("Warning", "Course ID and Name are required!")
                return

            if credits_text == "" or fee_text == "":
                messagebox.showwarning("Warning", "Credits and Tuition Fee are required!")
                return

            credits = int(credits_text)
            fee = float(fee_text)

            if credits <= 0 or fee < 0:
                messagebox.showwarning("Warning", "Credits and tuition fee must be valid!")
                return

            if course_type == "Compulsory":
                course = CompulsoryCourse(course_id, name, credits, fee)
            else:
                course = ElectiveCourse(course_id, name, credits, fee)

            if self.course_service.add_course(course, course_type):
                messagebox.showinfo("Success", "Course added successfully!")
                self.clear_form()
                self.load_courses()
            else:
                messagebox.showerror("Error", "Cannot add course!")

        except ValueError:
            messagebox.showerror("Error", "Credits must be integer and tuition fee must be number!")

    def update_course(self):
        try:
            course_id = self.get_value(self.entry_id, "Enter course id")
            name = self.get_value(self.entry_name, "Enter course name")
            credits_text = self.get_value(self.entry_credits, "Enter credits")
            fee_text = self.get_value(self.entry_fee, "Enter tuition fee")

            if course_id == "":
                messagebox.showwarning("Warning", "Please select a course!")
                return

            credits = int(credits_text)
            fee = float(fee_text)

            if credits <= 0 or fee < 0:
                messagebox.showwarning("Warning", "Credits and tuition fee must be valid!")
                return

            course = CompulsoryCourse(course_id, name, credits, fee)
            self.course_service.update_course(course)

            messagebox.showinfo("Success", "Course updated successfully!")
            self.clear_form()
            self.load_courses()

        except ValueError:
            messagebox.showerror("Error", "Credits must be integer and tuition fee must be number!")

    def delete_course(self):
        course_id = self.get_value(self.entry_id, "Enter course id")

        if course_id == "":
            messagebox.showwarning("Warning", "Please select a course!")
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this course?"):
            return

        self.course_service.delete_course(course_id)

        messagebox.showinfo("Success", "Course deleted successfully!")
        self.clear_form()
        self.load_courses()

    def clear_entry(self, entry, placeholder):
        entry.delete(0, tk.END)
        entry.insert(0, placeholder)
        entry.config(fg=COLORS["muted"])

    def clear_form(self):
        self.clear_entry(self.entry_id, "Enter course id")
        self.clear_entry(self.entry_name, "Enter course name")
        self.clear_entry(self.entry_credits, "Enter credits")
        self.clear_entry(self.entry_fee, "Enter tuition fee")
        self.course_type.set("Compulsory")
        self.load_courses()

    def on_select(self, event):
        selected_item = self.tree.selection()

        if selected_item:
            values = self.tree.item(selected_item[0], "values")

            entries = [
                (self.entry_id, values[0]),
                (self.entry_name, values[1]),
                (self.entry_credits, values[2]),
                (self.entry_fee, values[3])
            ]

            for entry, value in entries:
                entry.delete(0, tk.END)
                entry.insert(0, value)
                entry.config(fg=COLORS["text"])

            self.course_type.set(values[4])