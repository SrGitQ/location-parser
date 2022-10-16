import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
from utils import writeR, styleCharger, sidebarHidden

st.set_page_config(layout="wide")
styleCharger()
st.markdown("""
  <style>
    div[data-testid="stHorizontalBlock"]>div:first-child div.stButton,
    div[data-testid="stMarkdownContainer"]:has(button) {
      padding-left: 10rem;
      padding-top: 1.5rem;
    }
    div[data-testid="stHorizontalBlock"]>div:first-child button[kind="primary"] {
      color: #b7b9bc;
      border-radius: 100px;
    }
    div[data-testid="stMarkdownContainer"] button {
      color: #b7b9bc;
      border-radius: 100px;
    }
  <style>
""", unsafe_allow_html=True)

col_1, col_2, col_3 = st.columns([1, 1, 1])

with col_1:
  if st.button("<"):
  	switch_page("place_search")

with col_2:
  writeR("""
  <h1 style="text-align: center; font-family:helvetica">IMaP</h1>
  """)

writeR("""
  <iframe src="http://localhost:3000/" height="1530px" width="1400px" ></iframe>
""")

writeR("""
  <div class="row-widget stButton" style="width: 467px; color:#4d4d4d; "><a href="http://localhost:5000/file/dashboard.pdf"><button kind="primary" class="css-6kekos edgvbvh9">Download</button></a></div>
  <br>
  <br>
""")

sidebarHidden()
