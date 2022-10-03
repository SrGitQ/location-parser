import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils import sidebarHidden

#config streamlit to wide mode
st.set_page_config(layout="wide")

if 'place' not in st.session_state:
	st.session_state.place = 'main'

st.title("Home")
if st.button("list"):
	switch_page("list")
st.write(st.session_state.place)
st.markdown('''
	<iframe src="http://localhost:3000/" height="600vh" width="600vh" ></iframe>
''', unsafe_allow_html=True)

sidebarHidden()