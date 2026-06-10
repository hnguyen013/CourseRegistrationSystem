import tkinter as tk
from tkinter import ttk, messagebox

from models.lecturer import Lecturer
from services.lecturer_service import LecturerService
from views.style import COLORS, FONT_NORMAL, FONT_BOLD, apply_style, make_button

# 1. IMPORT LỚP BASEVIEW TỪ FILE BASE_VIEW
from views.base_view import BaseView


# 2. SỬA ĐỂ LỚP LECTURERVIEW KẾ THỪA TỪ BASEVIEW
class LecturerView(BaseView):
    def __init__(self):
        # 3. GỌI CONSTRUCTOR CỦA BASEVIEW VÀ TRUYỀN CÁC THAM SỐ GIAO DIỆN CHUẨN
        # Tham số theo thứ tự: title, current_page, icon_text, subtitle
        super().__init__(
            title="Lecturer Management",
            current_page="Lecturer",
            icon_text="👨‍🏫",
            subtitle="Manage lecturer information efficiently"
        )

        self.lecturer_service = LecturerService()

        # Khởi tạo phần giao diện đặc trưng và tải dữ liệu giảng viên
        self.create_widgets()
        self.load_lecturers()

    def create_widgets(self):
        # KHÔNG tạo lại container, sidebar, và header nữa vì BaseView đã xử lý hoàn chỉnh.
        # Ta gắn trực tiếp Form nhập và Bảng Treeview vào vùng chứa `self.content` của BaseView.

        # --- Khối nhập thông tin giảng viên (Form Card) ---
        form_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   👨‍🏫 Lecturer Information   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=25,
            pady=20
        )
        form_card.pack(fill="x", pady=(0, 16))

        self.entry_id = self.create_input(form_card, "Lecturer ID", 0, 0, "Enter lecturer id")
        self.entry_name = self.create_input(form_card, "Name", 0, 2, "Enter name")
        self.entry_email = self.create_input(form_card, "Email", 0, 4, "Enter email")
        self.entry_department = self.create_input(form_card, "Department", 0, 6, "Enter department")

        button_frame = tk.Frame(form_card, bg=COLORS["white"])
        button_frame.grid(row=2, column=0, columnspan=8, sticky="ew", pady=(20, 0))

        make_button(button_frame, "+   Add", self.add_lecturer, COLORS["success"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "✎   Update", self.update_lecturer, COLORS["info"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "🗑   Delete", self.delete_lecturer, COLORS["danger"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "↕   Sort ID", self.sort_by_id, COLORS["primary"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "A-Z Sort Name", self.sort_by_name, COLORS["primary"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)
        make_button(button_frame, "↻   Clear", self.clear_form, COLORS["gray"]).pack(side="left", fill="x", expand=True, padx=6, ipady=4)

        # --- Khối hiển thị danh sách giảng viên (List Card) ---
        list_card = tk.LabelFrame(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="   ▦ Lecturer List   ",
            bg=COLORS["white"],
            fg=COLORS["primary"],
            font=("Arial", 13, "bold"),
            padx=18,
            pady=16
        )
        list_card.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            list_card,
            columns=("lecturer_id", "name", "email", "department"),
            show="headings"
        )

        self.tree.heading("lecturer_id", text="Lecturer ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("department", text="Department")

        self.tree.column("lecturer_id", width=80, anchor="center")
        self.tree.column("name", width=280)
        self.tree.column("email", width=330)
        self.tree.column("department", width=250)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # --- Nhãn hiển thị tổng số lượng giảng viên ---
        self.lbl_total = tk.Label(
            self.content,  # Đổi sang self.content để kế thừa từ lớp cha
            text="👥   Total: 0 lecturers",
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

    def load_lecturers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        lecturers = self.lecturer_service.get_all_lecturers()

        for lecturer in lecturers:
            self.tree.insert("", tk.END, values=lecturer)

        self.lbl_total.config(text=f"👥   Total: {len(lecturers)} lecturers")

    def add_lecturer(self):
        lecturer_id = self.get_value(self.entry_id, "Enter lecturer id")
        name = self.get_value(self.entry_name, "Enter name")
        email = self.get_value(self.entry_email, "Enter email")
        department = self.get_value(self.entry_department, "Enter department")

        if lecturer_id == "" or name == "":
            messagebox.showwarning("Warning", "Lecturer ID and Name are required!")
            return

        lecturer = Lecturer(lecturer_id, name, email, department)

        if self.lecturer_service.add_lecturer(lecturer):
            messagebox.showinfo("Success", "Lecturer added successfully!")
            self.clear_form()
            self.load_lecturers()
        else:
            messagebox.showerror("Error", "Cannot add lecturer!")

    def update_lecturer(self):
        lecturer_id = self.get_value(self.entry_id, "Enter lecturer id")
        name = self.get_value(self.entry_name, "Enter name")
        email = self.get_value(self.entry_email, "Enter email")
        department = self.get_value(self.entry_department, "Enter department")

        if lecturer_id == "":
            messagebox.showwarning("Warning", "Please select a lecturer!")
            return

        lecturer = Lecturer(lecturer_id, name, email, department)
        self.lecturer_service.update_lecturer(lecturer)

        messagebox.showinfo("Success", "Lecturer updated successfully!")
        self.clear_form()
        self.load_lecturers()

    def delete_lecturer(self):
        lecturer_id = self.get_value(self.entry_id, "Enter lecturer id")

        if lecturer_id == "":
            messagebox.showwarning("Warning", "Please select a lecturer!")
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this lecturer?"):
            return

        self.lecturer_service.delete_lecturer(lecturer_id)

        messagebox.showinfo("Success", "Lecturer deleted successfully!")
        self.clear_form()
        self.load_lecturers()

    def clear_entry(self, entry, placeholder):
        entry.delete(0, tk.END)
        entry.insert(0, placeholder)
        entry.config(fg=COLORS["muted"])

    def clear_form(self):
        self.clear_entry(self.entry_id, "Enter lecturer id")
        self.clear_entry(self.entry_name, "Enter name")
        self.clear_entry(self.entry_email, "Enter email")
        self.clear_entry(self.entry_department, "Enter department")
        self.load_lecturers()

    def on_select(self, event):
        selected_item = self.tree.selection()

        if selected_item:
            values = self.tree.item(selected_item[0], "values")

            entries = [
                (self.entry_id, values[0]),
                (self.entry_name, values[1]),
                (self.entry_email, values[2]),
                (self.entry_department, values[3])
            ]

            for entry, value in entries:
                entry.delete(0, tk.END)
                entry.insert(0, value)
                entry.config(fg=COLORS["text"])
    def sort_by_id(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        lecturers = self.lecturer_service.sort_lecturers("id")

        for lecturer in lecturers:
            self.tree.insert("", tk.END, values=lecturer)

        self.lbl_total.config(text=f"👥   Sorted by Lecturer ID: {len(lecturers)} lecturers")


    def sort_by_name(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        lecturers = self.lecturer_service.sort_lecturers("name")

        for lecturer in lecturers:
            self.tree.insert("", tk.END, values=lecturer)

        self.lbl_total.config(text=f"👥   Sorted by Name: {len(lecturers)} lecturers")