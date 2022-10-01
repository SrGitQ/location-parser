import streamlit as st
def sidebarHidden():
	st.sidebar.markdown("""
		<style>
			#root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-1vencpc {
				display: none;
			}
		</style>
	""", unsafe_allow_html=True)