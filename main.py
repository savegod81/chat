import streamlit as st
message = []
if 'key' not in st.session_state:
    st.session_state['key'] = message
	

st.title("Our Private Chatroom")
input = st.text_input("Your Message1:")

all_msg = st.session_state.key
for msg in all_msg:
	st.write(msg)
