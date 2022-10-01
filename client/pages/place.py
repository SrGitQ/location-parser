import streamlit as st
from utils import sidebarHidden
from streamlit_extras.switch_page_button import switch_page

st.title("Tere tulemast")
if st.button("list"):
	switch_page("list")
st.write(st.session_state.place)
if st.button("change info"):
  st.session_state.place = 'info'
  switch_page("place")

sidebarHidden()
