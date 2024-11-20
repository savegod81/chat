import streamlit as st
if 'key' not in st.session_state:
    st.session_state['key'] = []

st.title("Our Private Chatroom")
input = st.text_input("Your Message2:")

all_msg = st.session_state.key
all_msg.append(input)
st.session_state['key'] = message
for msg in all_msg:
	st.write(msg)
