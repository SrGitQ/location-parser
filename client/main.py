import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils import writeR, sidebarHidden, headerRender, styleCharger, headerRender

#config streamlit to wide mode
st.set_page_config(layout="wide")
styleCharger()
headerRender('<h1 style="text-align: center; font-family:helvetica">IMaP</h1>')
headerRender('<br><br><p style="text-align: center; font-family:helvetica; color:#8e9297">Select an option...</p><br>')
# background-color: #f2f2f2;
writeR("""
  <style>
    div[data-testid="stHorizontalBlock"]>div:has(button):nth-of-type(2) .stButton {
      background: url("http://localhost:5000/icons/icon3.png");
      height: 320px;
      background-size:cover;
    }
    div[data-testid="stHorizontalBlock"]>div:has(button):nth-of-type(3) .stButton {
      background: url("http://localhost:5000/icons/icon4.png");
      height: 320px;
      background-size:cover;

    }
    .stButton button{
      background: transparent;
      width: 100%;
      height: 20rem;
    }
  <style>
""")

if 'search_place' not in st.session_state:
  st.session_state.search_place = ''

if 'search_compare' not in st.session_state:
  st.session_state.search_compare = ''

if 'places' not in st.session_state:
  st.session_state.places = []


col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col2:
  if st.button("", key='1'):
    switch_page("list")
  writeR('<p style="text-align: center; color:#8e9297; font-weight:bold; font-size:20px;">Compare places</p>')
with col3:
  if st.button("", key='2'):
    switch_page("searchPlace")
  writeR('<p style="text-align: center; color:#8e9297; font-weight:bold; font-size:20px;">Search my place</p>')

sidebarHidden()