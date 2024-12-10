import customtkinter as ctk
from tkinter import messagebox

# إعداد الواجهة
ctk.set_appearance_mode("System")  # الوضع (System, Dark, Light)
ctk.set_default_color_theme("blue")  # الثيم (blue, dark-blue, green)

# إنشاء النافذة الرئيسية
app = ctk.CTk()
app.title("Weather Vision Applications")
app.geometry("700x500")

# دالة لتشغيل الأكواد الخاصة بكل تطبيق
def run_application(app_name):
    messagebox.showinfo("Run Application", f"Running {app_name}...")
    # هنا تضيف الأكواد الخاصة بكل تطبيق
    if app_name == "Weather Prediction":
        pass  # استبدل بـ الكود الخاص
    elif app_name == "Cloud Detection":
        pass  # استبدل بـ الكود الخاص
    elif app_name == "Rainfall Estimation":
        pass  # استبدل بـ الكود الخاص
    elif app_name == "Storm Tracking":
        pass  # استبدل بـ الكود الخاص

# عنوان واجهة المستخدم
title_label = ctk.CTkLabel(
    app, 
    text="Weather Vision Applications",
    font=("Roboto", 28, "bold"),
    text_color="teal"
)
title_label.pack(pady=20)

# شرح واجهة المستخدم
subtitle_label = ctk.CTkLabel(
    app, 
    text="Explore cutting-edge applications of computer vision in weather analysis.",
    font=("Roboto", 16),
    text_color="gray"
)
subtitle_label.pack(pady=10)

# الإطارات الخاصة بكل تطبيق
applications = [
    "Weather Prediction",
    "Cloud Detection",
    "Rainfall Estimation",
    "Storm Tracking"
]

for app_name in applications:
    app_button = ctk.CTkButton(
        app,
        text=app_name,
        font=("Roboto", 18),
        fg_color="teal",
        hover_color="dark cyan",
        command=lambda name=app_name: run_application(name)
    )
    app_button.pack(pady=10, padx=20, fill="x")

# تشغيل التطبيق
app.mainloop()