import tkinter as tk
from tkinter import ttk

COLORS = {
    "bg": "#F4F7FA",
    "sidebar": "#065F5B",
    "sidebar_hover": "#0F766E",
    "primary": "#0F766E",
    "success": "#22C55E",
    "info": "#3B82F6",
    "danger": "#EF4444",
    "warning": "#F59E0B",
    "gray": "#6B7280",
    "white": "#FFFFFF",
    "text": "#1F2937",
    "muted": "#6B7280",
    "border": "#D1D5DB"
}

FONT_TITLE = ("Arial", 18, "bold")
FONT_NORMAL = ("Arial", 10)
FONT_BOLD = ("Arial", 10, "bold")


def apply_style(root):
    root.configure(bg=COLORS["bg"])

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Treeview",
        background=COLORS["white"],
        foreground=COLORS["text"],
        rowheight=28,
        fieldbackground=COLORS["white"],
        font=FONT_NORMAL,
        borderwidth=0
    )

    style.configure(
        "Treeview.Heading",
        background=COLORS["primary"],
        foreground=COLORS["white"],
        font=FONT_BOLD,
        padding=8
    )

    style.map(
        "Treeview",
        background=[("selected", "#99F6E4")],
        foreground=[("selected", COLORS["text"])]
    )


def make_button(parent, text, command, bg):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg="white",
        activebackground=bg,
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=12,
        pady=7,
        font=FONT_BOLD,
        cursor="hand2"
    )