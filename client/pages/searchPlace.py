import streamlit as st
from utils import writeR, sidebarHidden, styleCharger, headerRenderWithButton
from streamlit_extras.switch_page_button import switch_page
import requests
import json

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

def searchPlace(name, reference):
  API_KEY='AIzaSyCFXJsJDyC32kIJ2AHu2IMF1-osa6uKwSo'

  # Endpoint
  endpoint_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

  # Parameters
  params = {
      'query': name+reference,
      'key': API_KEY
  }
  # Request
  response = requests.get(endpoint_url, params = params)
  # Results
  results = json.loads(response.content)
  return results['results']

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
  writeR('<br><br>')
  name = st.text_input("Name of the place", placeholder="Cinepolis")
  address = st.text_input("Reference", placeholder="Caucel, Yucatán, 20.000, -81.000")
  writeR('<br><br>')
  if st.button("Search", key='search') and name and address:
    # places = requests.get('http://localhost:5000/places')
    st.session_state['search_place'] = searchPlace(name, address)
    # st.write(searchPlace(name, address))

    switch_page('place_search')
  elif st.session_state['search'] and not (name and address):
    writeR('<br><br>')
    st.warning('fill the data', icon="⚠️")

sidebarHidden()