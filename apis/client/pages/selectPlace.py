import re
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

col_1, col_2, col_3 = st.columns([1, 1, 1])
with col_1:
  if st.button("<"):
    # requests.get('http://localhost:5000/compare/reset')
    switch_page('compareSearch')

with col_2:
  writeR("""
  <h1 style="text-align: center; font-family:helvetica">IMaP</h1>
  """)
with col_3:
  writeR("""
    <style>
      div[data-testid="stHorizontalBlock"] div[data-testid="column"]:last-child div.stButton{
        padding-left: 10rem;
        padding-top: 1.5rem;
        border-radius: 30px;
        color: #b7b9bc;
      }
      div[data-testid="stHorizontalBlock"] div[data-testid="column"]:last-child div.stButton button{
        border-radius: 30px;
      }
    </style>
  """)
  if st.button('⌂'):
    requests.get('http://localhost:5000/compare/reset')
    switch_page('main')

def go_to_place(id_):
  card = st.empty()
  with card.container():
    st.write('hello'+id_)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
	writeR("""
	  <style>
	    div[data-testid="stVerticalBlock"]>div[style] div[data-testid="stVerticalBlock"]{
	      background-color: #f5f5f5;
	      padding: 1rem;
	      border-radius: 10px;
	      border: 1px solid #e6e6e6;
	    }
	    div[data-testid="stVerticalBlock"]>div[style] div[data-testid="stVerticalBlock"] p{
	      margin: 0px;
	    }
	    div[data-testid="stVerticalBlock"]>div[style] div[data-testid="stVerticalBlock"] p:first-child{
	      color: #494949;
	      font-weight: bold;
	    }
	    div[data-testid="stVerticalBlock"]>div[style] div[data-testid="stVerticalBlock"] p:not(:first-child){
	      color: #b7b9bc;
	    }
	    div[data-testid="stVerticalBlock"]>div[style] div[data-testid="stVerticalBlock"] button{
	      color: #b7b9bc;
	      width: 80px;
	      border-radius: 20px;
	      height: 20px;
	    }
	  </style>
	""")
	writeR('<br><br><p style="text-align: center; font-family:helvetica; color:#8e9297">Select the main place...</p><br>')
	current = []
	for id, place in enumerate(st.session_state.search_compare):
		content = st.empty()
		with content.container():
			writeR("""
			  <div>
			    <p>{}</p>
			    <p>{}</p>
			    <p>{}</p>
			  <div>
			""".format(place['name'], place['formatted_address'], place['types'][0]))

			if st.button('select', key=f'{id}_place'):		
				place_id = place['place_id']
				types = st.session_state['types']
				radius = st.session_state['radius']

				query = {
					'place_id': place_id,
					'types': types,
					'location':place['geometry']['location'],
					'radius': radius
				}

				requests.post('http://localhost:5000/competency/q', {'query': json.dumps(query)})

				switch_page('place')


sidebarHidden()
