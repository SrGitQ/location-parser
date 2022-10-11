import streamlit as st
from utils import sidebarHidden
from streamlit_extras.switch_page_button import switch_page

def writeR(text):
  st.markdown(text, unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.markdown("""
  <style>
    header[data-testid="stHeader"]{
      display: none;
    }
    footer[class]{
      display: none;
    }
    section>.block-container{
      padding: 0px;
    }

    button[kind="primary"]{
      color: #b7b9bc;
      border-radius: 100px;
    }
    div.stButton{
      padding-left: 10rem;
      padding-top: 1.5rem;
    }
  </style>
""" , unsafe_allow_html=True)

col_1, col_2, col_3 = st.columns([1, 1, 1])
with col_1:
  if st.button("<"):
  	switch_page("list")
with col_2:
  writeR("""
  <h1 style="text-align: center; font-family:helvetica">IMaP</h1>
  """)

writeR("""
  <iframe src="http://localhost:3000/" height="1900px" width="1400px" ></iframe>
""")



sidebarHidden()
