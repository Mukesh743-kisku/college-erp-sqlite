import streamlit as st
import sqlite3

st.title("Student Login")

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, roll_no TEXT, email TEXT, password TEXT,
              course TEXT, gender TEXT, address TEXT, dob TEXT,
              color TEXT, photo BLOB, admission_date TEXT)''')
conn.commit()

roll_no = st.text_input("Roll No").strip()
password = st.text_input("Password", type="password").strip()

if st.button("Login"):
    c.execute("SELECT * FROM students WHERE roll_no=? AND password=?", (roll_no, password))
    data = c.fetchone()

    if data:
        st.session_state['logged_in'] = True
        st.session_state['student_data'] = data
        st.success("Login Successful!")
        st.rerun()
    else:
        st.error("Galat Roll No ya Password bhai. Pehle SignUp karo.")

conn.close()

if 'logged_in' in st.session_state and st.session_state['logged_in']:
    st.success(f"Welcome {st.session_state['student_data'][0]}!")
    st.info("Ab Profile page pe jaa ke apna data dekh 👈")
