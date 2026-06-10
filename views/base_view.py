import tkinter as tk

from views.style import COLORS, apply_style


class BaseView(tk.Toplevel):
    def __init__(self, title, current_page, icon_text, subtitle):
        super().__init__()

        self.title(title)
        self.geometry("1200x720")
        self.minsize(1100, 650)

        apply_style(self)

        self.container = tk.Frame(self, bg=COLORS["bg"])
        self.container.pack(fill="both", expand=True)

        self.create_sidebar(current_page)

        self.content = tk.Frame(self.container, bg=COLORS["bg"])
        self.content.pack(side="left", fill="both", expand=True, padx=25, pady=20)

        self.create_header(icon_text, title, subtitle)

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
            ("🏠  Dashboard", "Dashboard", self.open_dashboard),
            ("👨‍🎓  Student", "Student", self.open_student_view),
            ("👨‍🏫  Lecturer", "Lecturer", self.open_lecturer_view),
            ("📚  Course", "Course", self.open_course_view),
            ("📝  Registration", "Registration", self.open_registration_view),
            ("📊  Reports", "Reports", self.open_report_view)
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
            text="⏻  Exit",
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

    def open_dashboard(self):
        from views.dashboard_view import DashboardView
        self.destroy()
        DashboardView()

    def open_student_view(self):
        from views.student_view import StudentView
        self.destroy()
        StudentView()

    def open_lecturer_view(self):
        from views.lecturer_view import LecturerView
        self.destroy()
        LecturerView()

    def open_course_view(self):
        from views.course_view import CourseView
        self.destroy()
        CourseView()

    def open_registration_view(self):
        from views.registration_view import RegistrationView
        self.destroy()
        RegistrationView()

    def open_report_view(self):
        from views.report_view import ReportView
        self.destroy()
        ReportView()