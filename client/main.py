import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils import sidebarHidden

if 'place' not in st.session_state:
	st.session_state.place = 'main'

st.title("Home")
if st.button("list"):
	switch_page("list")
st.write(st.session_state.place)
sidebarHidden()