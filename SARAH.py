import streamlit as st
from auth import show_auth_block


st.set_page_config(page_title="SARAH", layout="wide")

st.sidebar.success("Start Editing")

# login/logout
with st.sidebar:
    show_auth_block()

# SITE TITLE
st.title("SARAH: Story Analysis & Revision AI Helper")
# Derscription
st.markdown('''
**SARAH** is an **AI-powered developmental editing assistant** designed to help fiction authors refine their manuscripts with 
professional-grade insights, to support their storytelling and publishing goals.
''', width="stretch",)
st.divider()

