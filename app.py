import streamlit as st
# Navigation Panel
pg = st.navigation([st.Page("import.py"), st.Page("export.py")])
pg.run()
