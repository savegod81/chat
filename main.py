import streamlit as st
if 'key' not in st.session_state:
    st.session_state['key'] = []

messages = []

@st.cache_data
def get_conn():
	conn = st.connection('messages_db', type='sql')
	return conn

conn = get_conn()

def save(msg):
	with conn.session as s:
		s.execute('CREATE TABLE IF NOT EXISTS chat_messages(msg_ts timestamp, message TEXT);')
		s.execute(
    		'INSERT INTO chat_messages (msg_ts, message) VALUES (current_timestamp, :msg);',
            params=dict(msg=msg)
    	)
		s.commit()

def getAll():
	sql = 'select * from chat_messages order by msg_ts desc'
	results = conn.query(sql=sql, ttl=10)
	st.dataframe(results)

st.title("Our Private Chatroom")
input = st.text_input("Your Message1:")
save(input)

messages = getAll() 
st.write(messages)
