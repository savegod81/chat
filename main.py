import streamlit as st

messages = []

@st.cache_data
def save(msg):
	messages.append(msg)
	return messages

st.title("Our Private Chatroom")
input = st.text_input("Your Message:")

all_msg = save(input)
for msg in all_msg:
	st.write(msg)