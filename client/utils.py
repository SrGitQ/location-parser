import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def sidebarHidden():
	st.sidebar.markdown("""
		<style>
			section[data-testid="stSidebar"] {
				display: none;
			}
		</style>
	""", unsafe_allow_html=True)


def writeR(text):
  st.markdown(text, unsafe_allow_html=True)

def styleCharger():

  st.markdown("""
  <style>
    a {
      text-decoration: none;
    }
    header[data-testid="stHeader"]{
      display: none;
    }
    footer[class]{
      display: none;
    }
    section>.block-container{
      padding: 0px;
    }
  </style>
  """ , unsafe_allow_html=True)


def headerRenderWithButton(page):
  col_1, col_2, col_3 = st.columns([1, 1, 1])
  with col_1:
    if st.button("<"):
      switch_page(page)
  with col_2:
    writeR("""
    <h1 style="text-align: center; font-family:helvetica">IMaP</h1>
    """)

def headerRender(markdown):
  col_1, col_2, col_3 = st.columns([1, 1, 1])
  with col_1:
    pass
  with col_2:
    writeR(markdown)
  with col_3:
    pass


