import streamlit as st
from utils import sidebarHidden
from streamlit_extras.switch_page_button import switch_page

st.title("Some places")
if st.button("home"):
	switch_page("main")

if st.button("place"):
  switch_page("place")
sidebarHidden()
