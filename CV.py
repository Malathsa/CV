import streamlit as st

# إعداد الواجهة
st.set_page_config(page_title="Weather Vision Applications", layout="centered")

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

for app_name in applications:
    if st.button(app_name):
        run_application(app_name)
