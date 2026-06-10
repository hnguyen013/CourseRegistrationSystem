import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

from services.database_service import DatabaseService
from views.style import COLORS, apply_style, make_button

# 1. IMPORT LỚP BASEVIEW TỪ FILE BASE_VIEW
from views.base_view import BaseView


# 2. SỬA ĐỂ LỚP REPORTVIEW KẾ THỪA TỪ BASEVIEW
class ReportView(BaseView):
    def __init__(self):
        # 3. GỌI CONSTRUCTOR CỦA BASEVIEW VÀ TRUYỀN CÁC THAM SỐ GIAO DIỆN
        # Tham số theo thứ tự: title, current_page, icon_text, subtitle
        super().__init__(
            title="Reports",
            current_page="Reports",
            icon_text="📊",
            subtitle="Generate and export system reports"
        )

        self.db = DatabaseService()
        self.current_report = []

        # Khởi tạo giao diện đặc trưng cho trang báo cáo
        self.create_widgets()

    def create_widgets(self):
        # KHÔNG tạo lại container, sidebar, và header nữa vì BaseView đã chuẩn bị sẵn.
        # Ta gắn trực tiếp phần nút bấm chức năng và bảng hiển thị vào vùng chứa `self.content` của BaseView.

        # --- Khối hành động báo cáo (Action Card) ---
        report_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   📈 Report Actions   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=25,
            pady=20
        )
        report_card.pack(fill="x", pady=(0, 16))

        button_frame = tk.Frame(report_card, bg=COLORS["white"])
        button_frame.pack(fill="x")

        make_button(
            button_frame,
            "👨‍🎓 Student Tuition Report",
            self.student_tuition_report,
            COLORS["info"]
        ).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        make_button(
            button_frame,
            "📚 Course Registration Report",
            self.course_registration_report,
            COLORS["success"]
        ).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        make_button(
            button_frame,
            "💾 Export CSV",
            self.export_csv,
            COLORS["warning"]
        ).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        # --- Khối hiển thị kết quả (Table Card) ---
        table_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   ▦ Report Result   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=18,
            pady=16
        )
        table_card.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            table_card,
            show="headings"
        )

        self.tree.pack(fill="both", expand=True)

        # --- Nhãn trạng thái báo cáo ---
        self.lbl_info = tk.Label(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="📊 Ready to generate reports",
            bg=COLORS["bg"],
            fg=COLORS["primary"],
            font=("Arial", 11, "bold")
        )
        self.lbl_info.pack(anchor="w", pady=10)

    def set_columns(self, columns):
        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = columns

        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(
                col,
                width=250,
                anchor="center"
            )

    def student_tuition_report(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                students.student_id,
                students.name,
                IFNULL(SUM(courses.tuition_fee), 0)
            FROM students
            LEFT JOIN registrations
                ON students.student_id = registrations.student_id
            LEFT JOIN courses
                ON registrations.course_id = courses.course_id
            GROUP BY students.student_id, students.name
        """)

        rows = cursor.fetchall()

        conn.close()

        self.current_report = rows

        self.set_columns(
            ("student_id", "student_name", "total_tuition")
        )

        for row in rows:
            self.tree.insert("", tk.END, values=row)

        self.lbl_info.config(
            text=f"👨‍🎓 Student Tuition Report ({len(rows)} records)"
        )

    def course_registration_report(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                courses.course_id,
                courses.course_name,
                COUNT(registrations.student_id)
            FROM courses
            LEFT JOIN registrations
                ON courses.course_id = registrations.course_id
            GROUP BY courses.course_id, courses.course_name
        """)

        rows = cursor.fetchall()

        conn.close()

        self.current_report = rows

        self.set_columns(
            ("course_id", "course_name", "number_of_students")
        )

        for row in rows:
            self.tree.insert("", tk.END, values=row)

        self.lbl_info.config(
            text=f"📚 Course Registration Report ({len(rows)} records)"
        )

    def export_csv(self):
        if not self.current_report:
            messagebox.showwarning(
                "Warning",
                "Please generate a report first!"
            )
            return

        if not os.path.exists("exports"):
            os.makedirs("exports")

        file_path = os.path.join(
            "exports",
            "report.csv"
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                self.tree["columns"]
            )

            writer.writerows(
                self.current_report
            )

        messagebox.showinfo(
            "Success",
            f"Report exported successfully!\n\n{file_path}"
        )