import tkinter as tk
from tkinter import ttk, messagebox

from services.student_service import StudentService
from services.course_service import CourseService
from services.registration_service import RegistrationService
from views.style import COLORS, FONT_NORMAL, FONT_BOLD, apply_style, make_button

# 1. IMPORT LỚP BASEVIEW TỪ FILE BASE_VIEW
from views.base_view import BaseView


# 2. SỬA ĐỂ LỚP REGISTRATIONVIEW KẾ THỪA TỪ BASEVIEW
class RegistrationView(BaseView):
    def __init__(self):
        # 3. GỌI CONSTRUCTOR CỦA BASEVIEW VÀ TRUYỀN CÁC THAM SỐ GIAO DIỆN
        # Tham số theo thứ tự: title, current_page, icon_text, subtitle
        super().__init__(
            title="Course Registration",
            current_page="Registration",
            icon_text="📝",
            subtitle="Register students into available courses"
        )

        self.student_service = StudentService()
        self.course_service = CourseService()
        self.registration_service = RegistrationService()

        self.students = []
        self.courses = []

        # Khởi tạo giao diện đặc trưng và tải dữ liệu lên hệ thống
        self.create_widgets()
        self.load_combobox_data()
        self.load_registrations()

    def create_widgets(self):
        # KHÔNG tạo lại container, sidebar, và header nữa vì BaseView đã chuẩn bị sẵn.
        # Ta gắn trực tiếp phần Form Combobox và Bảng dữ liệu vào vùng chứa `self.content` của BaseView.

        # --- Khối thông tin đăng ký (Form Card) ---
        form_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   📝 Registration Information   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=25,
            pady=20
        )
        form_card.pack(fill="x", pady=(0, 16))

        tk.Label(
            form_card,
            text="Student",
            bg=COLORS["white"],
            fg=COLORS["text"],
            font=FONT_BOLD
        ).grid(row=0, column=0, sticky="w", padx=(0, 8), pady=6)

        self.cbo_student = ttk.Combobox(form_card, width=38, state="readonly", font=FONT_NORMAL)
        self.cbo_student.grid(row=1, column=0, columnspan=3, sticky="ew", padx=(0, 28), pady=6, ipady=5)

        tk.Label(
            form_card,
            text="Course",
            bg=COLORS["white"],
            fg=COLORS["text"],
            font=FONT_BOLD
        ).grid(row=0, column=3, sticky="w", padx=(0, 8), pady=6)

        self.cbo_course = ttk.Combobox(form_card, width=38, state="readonly", font=FONT_NORMAL)
        self.cbo_course.grid(row=1, column=3, columnspan=3, sticky="ew", padx=(0, 28), pady=6, ipady=5)

        # --- Khối nút chức năng ---
        button_frame = tk.Frame(form_card, bg=COLORS["white"])
        button_frame.grid(row=2, column=0, columnspan=6, sticky="ew", pady=(20, 0))

        make_button(button_frame, "+   Register", self.register_course, COLORS["success"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "↻   Refresh", self.refresh_data, COLORS["info"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        # --- Hiển thị tổng học phí ---
        self.lbl_total = tk.Label(
            form_card,
            text="Total Tuition: 0",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold")
        )
        self.lbl_total.grid(row=3, column=0, columnspan=6, sticky="w", pady=(18, 0))

        # --- Khối bảng danh sách đăng ký môn học (List Card) ---
        list_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   ▦ Registration List   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=18,
            pady=16
        )
        list_card.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            list_card,
            columns=("registration_id", "student_id", "student_name", "course_id", "course_name", "credits", "fee", "date"),
            show="headings"
        )

        headings = {
            "registration_id": "ID",
            "student_id": "Student ID",
            "student_name": "Student Name",
            "course_id": "Course ID",
            "course_name": "Course Name",
            "credits": "Credits",
            "fee": "Fee",
            "date": "Date"
        }

        for col, text in headings.items():
            self.tree.heading(col, text=text)

        self.tree.column("registration_id", width=60, anchor="center")
        self.tree.column("student_id", width=100, anchor="center")
        self.tree.column("student_name", width=180)
        self.tree.column("course_id", width=100, anchor="center")
        self.tree.column("course_name", width=250)
        self.tree.column("credits", width=80, anchor="center")
        self.tree.column("fee", width=130, anchor="center")
        self.tree.column("date", width=130, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # --- Nhãn hiển thị tổng số lượt đăng ký ---
        self.lbl_count = tk.Label(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="📝   Total: 0 registrations",
            bg=COLORS["bg"],
            fg=COLORS["primary"],
            font=("Arial", 11, "bold")
        )
        self.lbl_count.pack(anchor="w", pady=10)

    def load_combobox_data(self):
        self.students = self.student_service.get_all_students()
        self.courses = self.course_service.get_all_courses()

        self.cbo_student["values"] = [f"{s[0]} - {s[1]}" for s in self.students]
        self.cbo_course["values"] = [f"{c[0]} - {c[1]}" for c in self.courses]

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

        registrations = self.registration_service.get_all_registrations()

        for reg in registrations:
            self.tree.insert("", tk.END, values=reg)

        self.lbl_count.config(text=f"📝   Total: {len(registrations)} registrations")

    def refresh_data(self):
        self.load_combobox_data()
        self.load_registrations()
        self.lbl_total.config(text="Total Tuition: 0")