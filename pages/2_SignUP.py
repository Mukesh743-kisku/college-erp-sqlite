import streamlit as st
import sqlite3
from datetime import datetime

st.title("Student SignUp")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
course = st.selectbox("Course", ["BCA", "MCA", "BBA", "MBA"])
gender = st.radio("Gender", ["Male", "Female", "Other"])
address = st.text_area("Address")
dob = st.date_input("Date of Birth")
color = st.color_picker("Favorite Color", "#00f900")
picture = st.camera_input("Take a picture")

if st.button("Sign Up"):
    if name and password:
        roll_no = f"{course}{datetime.now().strftime('%Y%m%d%H%M%S')}"
        img_bytes = picture.getvalue() if picture else None

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS students
                     (name TEXT, roll_no TEXT, email TEXT, password TEXT,
                      course TEXT, gender TEXT, address TEXT, dob TEXT,
                      color TEXT, photo BLOB, admission_date TEXT)''')

        c.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                  (name, roll_no, email, password, course, gender, address,
                   str(dob), color, img_bytes, str(datetime.now())))

        conn.commit()
        conn.close()

        st.success(f"SignUp successful! Apka Roll No: {roll_no}")
        st.balloons()
        st.code(roll_no, language=None)
    else:
        st.error("Name aur Password to daalo bhai")
