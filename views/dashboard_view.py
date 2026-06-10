import tkinter as tk
from views.style import COLORS, apply_style, make_button

# Import các view để chuyển trang khi bấm nút menu
from views.student_view import StudentView
from views.lecturer_view import LecturerView
from views.course_view import CourseView
from views.registration_view import RegistrationView
from views.report_view import ReportView


class DashboardView(tk.Tk):  # Giữ tk.Tk vì đây là cửa sổ chạy đầu tiên của ứng dụng
    def __init__(self):
        super().__init__()

        # Đồng bộ kích thước giống hệt các trang quản lý
        self.title("Course Registration System")
        self.geometry("1200x720")
        self.minsize(1100, 650)

        apply_style(self)

        # Tạo cấu trúc container chính giống BaseView
        self.container = tk.Frame(self, bg=COLORS["bg"])
        self.container.pack(fill="both", expand=True)

        # 1. Tạo Sidebar (Đang active ở trang Dashboard)
        self.create_sidebar("Dashboard")

        # 2. Tạo Content Area
        self.content = tk.Frame(self.container, bg=COLORS["bg"])
        self.content.pack(side="left", fill="both", expand=True, padx=25, pady=20)

        # 3. Tạo Header
        self.create_header("🏠", "System Dashboard", "Welcome to the Course Registration System")

        # 4. Vẽ các thành phần nội dung của Dashboard
        self.create_widgets()

    def create_sidebar(self, current_page):
        sidebar = tk.Frame(self.container, bg=COLORS["sidebar"], width=170)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="MENU",
            bg=COLORS["sidebar"],
            fg="white",
            font=("Arial", 16, "bold")
        ).pack(pady=35)

        menu_items = [
            ("🏠   Dashboard", "Dashboard", self.open_dashboard),
            ("👨‍🎓   Student", "Student", self.open_student_view),
            ("👨‍🏫   Lecturer", "Lecturer", self.open_lecturer_view),
            ("📚   Course", "Course", self.open_course_view),
            ("📝   Registration", "Registration", self.open_registration_view),
            ("📊   Reports", "Reports", self.open_report_view)
        ]

        for text, page_name, command in menu_items:
            active = page_name == current_page

            tk.Button(
                sidebar,
                text=text,
                command=command,
                bg=COLORS["sidebar_hover"] if active else COLORS["sidebar"],
                fg="white",
                activebackground=COLORS["sidebar_hover"],
                activeforeground="white",
                relief="flat",
                bd=0,
                font=("Arial", 11, "bold"),
                anchor="w",
                padx=20,
                pady=12,
                cursor="hand2"
            ).pack(fill="x", padx=10, pady=4)

        tk.Button(
            sidebar,
            text="⏻   Exit",
            bg=COLORS["sidebar"],
            fg="white",
            activebackground=COLORS["danger"],
            activeforeground="white",
            relief="flat",
            bd=0,
            font=("Arial", 11, "bold"),
            command=self.destroy,
            cursor="hand2"
        ).pack(side="bottom", fill="x", padx=10, pady=30)

    def create_header(self, icon_text, title, subtitle):
        header = tk.Frame(self.content, bg=COLORS["bg"])
        header.pack(fill="x")

        tk.Label(
            header,
            text=icon_text,
            bg=COLORS["primary"],
            fg="white",
            font=("Arial", 22, "bold"),
            width=3,
            height=1
        ).pack(side="left", padx=(0, 15))

        title_box = tk.Frame(header, bg=COLORS["bg"])
        title_box.pack(side="left")

        tk.Label(
            title_box,
            text=title,
            bg=COLORS["bg"],
            fg=COLORS["primary"],
            font=("Arial", 24, "bold")
        ).pack(anchor="w")

        tk.Label(
            title_box,
            text=subtitle,
            bg=COLORS["bg"],
            fg=COLORS["muted"],
            font=("Arial", 12)
        ).pack(anchor="w")

        tk.Frame(
            self.content,
            bg=COLORS["border"],
            height=1
        ).pack(fill="x", pady=18)

    def create_widgets(self):
        # Thiết kế các ô thống kê (Cards) trực quan cho Dashboard đẹp mắt hơn thay vì chỉ có nút bấm thô sơ
        cards_frame = tk.Frame(self.content, bg=COLORS["bg"])
        cards_frame.pack(fill="x", pady=10)

        # Định nghĩa thông tin các Thẻ chức năng (Tên, Icon, Màu sắc, Hàm kích hoạt)
        features = [
            ("Student Management", "👨‍🎓", COLORS["success"], self.open_student_view),
            ("Lecturer Management", "👨‍🏫", COLORS["info"], self.open_lecturer_view),
            ("Course Management", "📚", COLORS["primary"], self.open_course_view),
            ("Course Registration", "📝", COLORS["warning"], self.open_registration_view),
            ("System Reports", "📊", COLORS["gray"], self.open_report_view)
        ]

        # Khởi tạo các Grid ô chức năng (mỗi hàng hiển thị tối đa 3 ô)
        for index, (name, icon, color, command) in enumerate(features):
            row = index // 3
            col = index % 3

            # Tạo khung cho từng ô (Card)
            card = tk.LabelFrame(
                cards_frame,
                bg=COLORS["white"],
                bd=1,
                relief="solid",
                padx=20,
                pady=20
            )
            card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

            # Label Icon của Thẻ
            tk.Label(
                card,
                text=icon,
                font=("Arial", 36),
                bg=COLORS["white"],
                fg=color
            ).pack(anchor="w", pady=(0, 5))

            # Label Tên chức năng
            tk.Label(
                card,
                text=name,
                font=("Arial", 14, "bold"),
                bg=COLORS["white"],
                fg=COLORS["text"]
            ).pack(anchor="w", pady=(0, 15))

            # Nút bấm mở điều hướng trang tương ứng
            make_button(card, "Open Link →", command, color).pack(fill="x", ipady=3)

        # Cấu hình để các ô giãn đều khoảng cách tự động
        for i in range(3):
            cards_frame.columnconfigure(i, weight=1)

    # --- LOGIC ĐIỀU HƯỚNG CHUYỂN TRANG ---
# --- CƠ CHẾ ĐIỀU HƯỚNG ẨN / HIỆN ĐÃ SỬA LỖI MESSAGEBOX ---
    def open_dashboard(self):
        pass  

    def open_student_view(self):
        self.withdraw()  # Ẩn Dashboard đi
        view = StudentView()
        
        # Hàm kiểm tra xem có đúng là trang Student bị đóng hoàn toàn hay không
        def on_close(event):
            # event.widget == view đảm bảo CHỈ khi trang Student đóng thì mới hiện Dashboard
            # Tránh bị bắt nhầm sự kiện khi đóng các hộp thoại messagebox
            if event.widget == view:
                self.deiconify()
                
        view.bind("<Destroy>", on_close)

    def open_lecturer_view(self):
        self.withdraw()
        view = LecturerView()
        
        def on_close(event):
            if event.widget == view:
                self.deiconify()
                
        view.bind("<Destroy>", on_close)

    def open_course_view(self):
        self.withdraw()
        view = CourseView()
        
        def on_close(event):
            if event.widget == view:
                self.deiconify()
                
        view.bind("<Destroy>", on_close)

    def open_registration_view(self):
        self.withdraw()
        view = RegistrationView()
        
        def on_close(event):
            if event.widget == view:
                self.deiconify()
                
        view.bind("<Destroy>", on_close)

    def open_report_view(self):
        self.withdraw()
        view = ReportView()
        
        def on_close(event):
            if event.widget == view:
                self.deiconify()
                
        view.bind("<Destroy>", on_close)
if __name__ == "__main__":
    app = DashboardView()
    app.mainloop()