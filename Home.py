import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Marwari College ERP", page_icon="🎓", layout="wide")

# Logo + Title side by side
col1, col2, col3 = st.columns([1,3,1])

with col1:
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🎓</h1>", unsafe_allow_html=True)
    logo_path = "assets/logo.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=120)
    else:
        st.write("🎓") # Logo nahi mila to emoji

with col2:
    st.title("Marwari College ERP System")
    st.subheader("Student Management Portal")

st.markdown("---")

st.info("👈 Sidebar se Login ya SignUp select karein")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Marwari College, Ranchi | Developed by vivenmusky</p>", unsafe_allow_html=True)
