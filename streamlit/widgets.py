import streamlit as st

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")