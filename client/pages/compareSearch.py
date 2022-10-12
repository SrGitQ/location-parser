import streamlit as st
from utils import writeR, sidebarHidden, headerRender, styleCharger, headerRenderWithButton
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

import requests
import json

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

headerRenderWithButton('main')
types = ["accounting","airport","amusement_park","aquarium","art_gallery","atm","bakery","bank","bar","beauty_salon","bicycle_store","book_store","bowling_alley","bus_station","cafe","campground","car_dealer","car_rental","car_repair","car_wash","casino","cemetery","church","city_hall","clothing_store","convenience_store","courthouse","dentist","department_store","doctor","drugstore","electrician","electronics_store","embassy","fire_station","florist","funeral_home","furniture_store","gas_station","gym","hair_care","hardware_store","hindu_temple","home_goods_store","hospital","insurance_agency","jewelry_store","laundry","lawyer","library","light_rail_station","liquor_store","local_government_office","locksmith","lodging","meal_delivery","meal_takeaway","mosque","movie_rental","movie_theater","moving_company","museum","night_club","painter","park","parking","pet_store","pharmacy","physiotherapist","plumber","police","post_office","primary_school","real_estate_agency","restaurant","roofing_contractor","rv_park","school","secondary_school","shoe_store","shopping_mall","spa","stadium","storage","store","subway_station","supermarket","synagogue","taxi_stand","tourist_attraction","train_station","transit_station","travel_agency","university","veterinary_care","zoo"]
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
  writeR('<br><br>')
  name = st.text_input("Name of the place", placeholder="Cinepolis")
  address = st.text_input("Reference", placeholder="Caucel, Yucatán, 20.000, -81.000")
  types = st.multiselect('Types of restaurants', types)
  radius = st.slider('Radius', min_value=1000, max_value=100000, value=1000)
  st.session_state['radius'] = radius
  st.session_state['types'] = types
  writeR('<br><br>')
  if st.button("Search", key='search') and name and address and types:
    st.session_state['search_compare'] = searchPlace(name, address)
    switch_page('selectPlace')
  elif st.session_state['search'] and not (name and address and types):
    writeR('<br><br>')
    st.warning('fill the data', icon="⚠️")

sidebarHidden()