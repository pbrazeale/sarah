import streamlit as st
from auth import show_auth_block

# login/logout
with st.sidebar:
    show_auth_block()
# Check authentication
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Export Title
st.title("Export")
st.markdown('''
**SARAH** will upload her edits here for you to download.
''', width="stretch",)
st.divider()