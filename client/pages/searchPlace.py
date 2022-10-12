import streamlit as st
from utils import writeR, sidebarHidden, styleCharger, headerRenderWithButton
from streamlit_extras.switch_page_button import switch_page
import requests

st.markdown("""
  <style>
    div[data-testid="stHorizontalBlock"]>div:first-child div.stButton{
      padding-left: 10rem;
      padding-top: 1.5rem;
    }
    div[data-testid="stHorizontalBlock"]>div:first-child button[kind="primary"]{
      color: #b7b9bc;
      border-radius: 100px;
    }
  <style>
""", unsafe_allow_html=True)
styleCharger()
headerRenderWithButton('main')

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
  writeR('<br><br>')
  name = st.text_input("Name of the place", placeholder="Cinepolis")
  address = st.text_input("Reference", placeholder="Caucel, Yucatán, 20.000, -81.000")
  writeR('<br><br>')
  if st.button("Search") and name and address:
    places = requests.get('http://localhost:5000/places')
    st.session_state['search_place'] = places.json()
    switch_page('place_search')
  elif not (name and address):
    writeR('<br><br>')
    st.warning('fill the data', icon="⚠️")

sidebarHidden()