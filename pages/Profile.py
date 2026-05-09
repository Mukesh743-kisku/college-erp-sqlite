import streamlit as st
from PIL import Image
import io

st.title("Student Profile")

# Session check karo
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please login first to view your profile.")
    st.stop()

# Data nikalo session se
data = st.session_state['student_data']
# data = (name, roll_no, email, password, course, gender, address, dob, color, photo, admission_date)

col1, col2 = st.columns([1,2])

with col1:
    st.subheader("Profile Photo")
    if data[9]: # photo BLOB
        try:
            image = Image.open(io.BytesIO(data[9]))
            st.image(image, width=200)
        except:
            st.image("https://via.placeholder.com/200", caption="Photo Error")
    else:
        st.image("https://via.placeholder.com/200", caption="No Photo")

with col2:
    st.subheader(data[0]) # Name
    st.write(f"**Roll No:** `{data[1]}`")
    st.write(f"**Course:** {data[4]}")
    st.write(f"**Email:** {data[2]}")
    st.write(f"**Gender:** {data[5]}")
    st.write(f"**DOB:** {data[7]}")
    st.write(f"**Address:** {data[6]}")
    st.write(f"**Admission Date:** {data[10][:10]}") # Date only

st.markdown("---")

if st.button("Logout"):
    st.session_state['logged_in'] = False
    st.session_state['student_data'] = None
    st.success("Logged out successfully!")
    st.rerun()
