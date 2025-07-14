import streamlit as st
from auth import show_auth_block

# Page config
st.set_page_config(page_title="Parameters", layout="wide")

# login/logout
with st.sidebar:
    show_auth_block()

# Require login
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# --- Store values in session state so they're accessible before input section ---
if "pov" not in st.session_state:
    st.session_state.pov = "1st Person"
if "tense" not in st.session_state:
    st.session_state.tense = "Present"
if "primary_genre" not in st.session_state:
    st.session_state.primary_genre = "Romance"
if "sub_genre" not in st.session_state:
    st.session_state.sub_genre = ""
if "main_character" not in st.session_state:
    st.session_state.main_character = ""

# --- Display Summary (first!) ---
st.title("⚙️ Parameters")

st.markdown("### 📋 Summary")

prefs = st.session_state.get("saved_prefs", {
    "Point of View": st.session_state.pov,
    "Tense": st.session_state.tense,
    "Genre": st.session_state.primary_genre,
    "Sub-Genre": st.session_state.sub_genre,
    "Main Character": st.session_state.main_character
})

st.write(f"#### Point of View: {prefs['Point of View']}")
st.write(f"#### Tense: {prefs['Tense']}")
st.write(f"#### Genre: {prefs['Genre']}" + 
         (f" > {prefs['Sub-Genre']}" if prefs['Sub-Genre'] else ""))
st.write(f"#### Main Character: {prefs['Main Character']}")
st.divider()


# --- Input Controls ---
# 1. Point of View
st.subheader("1. Point of View")
st.session_state.pov = st.radio("Choose the narrative perspective:", [
    "1st Person",
    "Limited 3rd Person",
    "Omniscient 3rd Person"
], horizontal=True)

# 2. Tense
st.subheader("2. Tense")
st.session_state.tense = st.radio("Choose the tense of narration:", [
    "Present",
    "Past"
], horizontal=True)

# 3. Genre Selection
st.subheader("3. Genre Selection")
genre_options = {
    "Romance": ["Contemporary", "Historical", "Paranormal", "Romantic Comedy"],
    "Mystery": ["Cozy", "Detective", "Noir", "Paranormal"],
    "Thriller": ["Psychological", "Political", "Action", "Crime", "Legal"],
    "Science Fiction": [],
    "Fantasy": ["Epic", "Urban", "Sword & Sorcery"],
    "Horror": []
}

st.session_state.primary_genre = st.selectbox("Primary Genre:", list(genre_options.keys()))
if genre_options[st.session_state.primary_genre]:
    st.session_state.sub_genre = st.selectbox("Sub-Genre:", genre_options[st.session_state.primary_genre])
else:
    st.session_state.sub_genre = ""

# 4. Main Character
st.subheader("4. Main Character")
st.session_state.main_character = st.text_input("Main Character Name:")

# --- Save Button ---
if st.button("💾 Save Preferences"):
    st.session_state.saved_prefs = {
        "Point of View": st.session_state.pov,
        "Tense": st.session_state.tense,
        "Genre": st.session_state.primary_genre,
        "Sub-Genre": st.session_state.sub_genre,
        "Main Character": st.session_state.main_character
    }
    st.success("✅ Preferences saved!")
    st.rerun()
