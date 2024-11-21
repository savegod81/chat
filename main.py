
import streamlit as st 
from sqlalchemy import text
@st.cache
def getConn():
	return st.connection('messages_db', type='sql')
conn = getConn()
CREATE_TBL = text('CREATE TABLE IF NOT EXISTS chat_messages(msg_ts timestamp, message TEXT);')
INSERT_SQL = text('INSERT INTO chat_messages (msg_ts, message) VALUES (current_timestamp, :msg);')
CLEAN_SQL = text('DELETE from chat_messages;')

def save(msg):
	with conn.session as s:
		s.execute(CREATE_TBL)
		s.execute(INSERT_SQL,
            params=dict(msg=msg)
    )
		s.commit()

def getAll():
	sql = 'select * from chat_messages order by msg_ts desc'
	results = conn.query(sql=sql, ttl=10)
	return results

def showMessage():
	messages = getAll() 
	if not messages.empty:
		st.write("New message...")
		st.dataframe(messages, width=800)

def clearit():
	input = st.session_state.msg
	print("input",input)
	save(input)
	st.session_state.msg = ""
	showMessage()


def clean():
	with conn.session as s:
		s.execute(CLEAN_SQL) 
		s.commit()


st.title("Our Private Chatroom")
input = st.text_input("Your Message:", key="msg",on_change=clearit)

if st.button("Clear It!"):
	clean()

