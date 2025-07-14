import streamlit as st
from auth import show_auth_block

# login/logout
with st.sidebar:
    show_auth_block()
# Check authentication
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Import Title
st.title("Import")
st.markdown('''
Import your manuscript for **SARAH** and her team to analyze.
''', width="stretch",)
st.divider()