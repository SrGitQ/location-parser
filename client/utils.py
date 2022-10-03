import streamlit as st
def sidebarHidden():
	st.sidebar.markdown("""
		<style>
			section[data-testid="stSidebar"] {
				display: none;
			}
		</style>
	""", unsafe_allow_html=True)