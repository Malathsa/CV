import streamlit as st
import base64

# إعداد الواجهة
st.set_page_config(page_title="Weather Vision Applications", layout="centered")

# إضافة الصورة كخلفية
def add_background(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# قراءة الصورة وإضافتها كخلفية
add_background("background.jpg")  # تأكد من وجود ملف الصورة بنفس المسار

# محتوى الواجهة
st.title("Weather Vision Applications")
st.subheader("Explore cutting-edge applications of computer vision in weather analysis.")

# دالة لتشغيل التطبيقات
def run_application(app_name):
    st.write(f"Running {app_name}...")
    # هنا تضيف الأكواد الخاصة بكل تطبيق
    if app_name == "Weather Prediction":
        st.write("Running Weather Prediction code...")
    elif app_name == "Cloud Detection":
        st.write("Running Cloud Detection code...")
    elif app_name == "Rainfall Estimation":
        st.write("Running Rainfall Estimation code...")
    elif app_name == "Storm Tracking":
        st.write("Running Storm Tracking code...")

# إنشاء الأزرار الخاصة بكل تطبيق
applications = [
    "Weather Prediction",
    "Cloud Detection",
    "Rainfall Estimation",
    "Storm Tracking"
]

# عرض الأزرار وتشغيل التطبيقات
for app_name in applications:
    if st.button(app_name):
        run_application(app_name)
