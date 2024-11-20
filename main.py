import streamlit as st
if 'key' not in st.session_state:
    st.session_state['key'] = []

messages = []

@st.cache_data
def save(msg):
	messages.append(msg)
	return messages

st.title("Our Private Chatroom")
input = st.text_input("Your Message1:")

all_msg = st.session_state.key
all_msg.append(input)
st.session_state['key'] = all_msg
for msg in all_msg:
	st.write(msg)
