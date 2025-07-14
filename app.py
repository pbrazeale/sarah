import streamlit as st
# Navigation Panel
pg = st.navigation([st.Page("home.py"), st.Page("import.py"), st.Page("export.py")])
pg.run()
