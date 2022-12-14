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

headerRenderWithButton('searchPlace')

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
  writeR('<br><br><p style="text-align: center; font-family:helvetica; color:#8e9297">Select a place...</p>')
  for id, place in enumerate(st.session_state.search_place):
    content = st.empty()
    with content.container():
      writeR("""
        <div>
          <p>{}</p>
          <p>{}</p>
          <p>{}</p>
        <div>
      """.format(place['name'], place['formatted_address'], place['types'][0]))
      if st.button('Go', key=f'{id}_place'):
        requests.get(f'http://localhost:5000/place/{place["place_id"]}')
        switch_page('place')


sidebarHidden()