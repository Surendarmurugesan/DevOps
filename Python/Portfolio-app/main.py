import streamlit as st
import pandas

st.markdown("# Home")
st.sidebar.markdown("# Home")
#st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Surendar Murugesan")
    content = """
    Hello, I am Surendar Murugesan! I am working as a DevOps Engineer. I graduated in 2017 with Bachelor's degree from Anna University.
    I have worked with Genesys company in Chennai.
    Four & Half years accomplished experience in Multi-cloud Administration, Orchestration, Infrastructure management, Automation,
    CI/CD, Monitoring and Architecting cloud infrastructure solutions.
    """
    st.info(content)

content = """Below you can find some of the apps I have built in Python. Feel free to contact me!!"""
st.write(content)

col3, empty_col, col4 = st.columns([2, 0.5, 2])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/" + row["image"])
        st.write(f"[Source code]({row['url']})")


#     st.title("Todo App")
#     description = """A distraction-free web app to help you on focus on creating and completing tasks."""
#     st.write(description)
#     st.image("images/1.png")
#
#     st.title("Portfolio Website")
#     portfolio_description = """
#     A website built entirely in Python to showcase coding projects and apps."""
#     st.write(portfolio_description)
#     st.image("images/2.png")
#
# with col4:
#     st.title("Webcam Motion Detector")
#     description = """
#     A program that monitors the computer webcam and sends an email when a new object enters the view.
#     """
#     st.write(description)
#     st.image("images/11.png")
#
#     st.title("Typing Analyzer")
#     Analyzer_description = """
#         A program that monitors the computer keyboard and returns the most typed words of the session."""
#     st.write(Analyzer_description)
#     st.image("images/12.png")

st.markdown("# Contact Us")
st.sidebar.markdown("# Contact Us")

st.text_input('Your email address', '')
st.text_input('Your message', '')

st.button("Submit")
# left_column.button('Submit')
