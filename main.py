import streamlit as st

st.title("Our Private Chatroom")
input = st.text_input("Your Message:")

st.write(input)