import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Surendar Murugesan")
    content = """
    Hello, I am Surendar Murugesan! I am working as a DevOps Engineer. I graduated in 2017 with Bachelor's degree from Anna University.
    I have worked with Genesys company in Chennai.
    """
    st.info(content)