import streamlit as st
import os
import json
from auth import show_auth_block

st.set_page_config(page_title="Parameters", layout="wide")

with st.sidebar:
    show_auth_block()

if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Saved Parameters
import_dir = "./working_dir/import"
os.makedirs(import_dir, exist_ok=True)
param_path = os.path.join(import_dir, "parameters.json")

# --- Load parameters from file if available ---
if "params_loaded" not in st.session_state:
    if os.path.exists(param_path):
        with open(param_path, "r", encoding="utf-8") as f:
            loaded_prefs = json.load(f)
        st.session_state.pov = loaded_prefs.get("Point of View", "1st Person")
        st.session_state.tense = loaded_prefs.get("Tense", "Present")
        st.session_state.primary_genre = loaded_prefs.get("Genre", "Romance")
        st.session_state.sub_genre = loaded_prefs.get("Sub-Genre", "")
        st.session_state.main_character = loaded_prefs.get("Main Character", "")
        st.session_state.saved_prefs = loaded_prefs
    else:
        # Defaults
        st.session_state.pov = "1st Person"
        st.session_state.tense = "Present"
        st.session_state.primary_genre = "Romance"
        st.session_state.sub_genre = ""
        st.session_state.main_character = ""
        st.session_state.saved_prefs = {}
    st.session_state.params_loaded = True

# # --- Store values in session state so they're accessible before input section ---
# if "pov" not in st.session_state:
#     st.session_state.pov = "1st Person"
# if "tense" not in st.session_state:
#     st.session_state.tense = "Present"
# if "primary_genre" not in st.session_state:
#     st.session_state.primary_genre = "Romance"
# if "sub_genre" not in st.session_state:
#     st.session_state.sub_genre = ""
# if "main_character" not in st.session_state:
#     st.session_state.main_character = ""

st.title("⚙️ Parameters")

st.markdown("### 📋 Summary")

prefs = {
    "Point of View": st.session_state.get("pov", "1st Person"),
    "Tense": st.session_state.get("tense", "Present"),
    "Genre": st.session_state.get("primary_genre", "Romance"),
    "Sub-Genre": st.session_state.get("sub_genre", ""),
    "Main Character": st.session_state.get("main_character", "")
}

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
    "1st Person", "Limited 3rd Person", "Omniscient 3rd Person"
], index=["1st Person", "Limited 3rd Person", "Omniscient 3rd Person"].index(st.session_state.pov), horizontal=True)

# 2. Tense
st.subheader("2. Tense")
st.session_state.tense = st.radio("Choose the tense of narration:", [
    "Present", "Past"
], index=["Present", "Past"].index(st.session_state.tense), horizontal=True)

# 3. Genere
st.subheader("3. Genre Selection")
genre_options = {
    "Romance": ["Contemporary", "Historical", "Paranormal", "Romantic Comedy"],
    "Mystery": ["Cozy", "Detective", "Noir", "Paranormal"],
    "Thriller": ["Psychological", "Political", "Action", "Crime", "Legal"],
    "Science Fiction": [],
    "Fantasy": ["Epic", "Urban", "Sword & Sorcery"],
    "Horror": []
}

st.session_state.primary_genre = st.selectbox("Primary Genre:", list(genre_options.keys()),
                                              index=list(genre_options.keys()).index(st.session_state.primary_genre))

if genre_options[st.session_state.primary_genre]:
    st.session_state.sub_genre = st.selectbox("Sub-Genre:", genre_options[st.session_state.primary_genre],
                                              index=genre_options[st.session_state.primary_genre].index(st.session_state.sub_genre)
                                              if st.session_state.sub_genre in genre_options[st.session_state.primary_genre] else 0)
else:
    st.session_state.sub_genre = ""

# 3. Main Character
st.subheader("4. Main Character")
st.session_state.main_character = st.text_input("Main Character Name:", value=st.session_state.main_character)


# --- Save Button ---
if st.button("💾 Save Preferences"):
    preferences = {
        "Point of View": st.session_state.pov,
        "Tense": st.session_state.tense,
        "Genre": st.session_state.primary_genre,
        "Sub-Genre": st.session_state.sub_genre,
        "Main Character": st.session_state.main_character
    }
    st.session_state.saved_prefs = preferences

    with open(param_path, "w", encoding="utf-8") as f:
        json.dump(preferences, f, indent=2)

    st.success("✅ Preferences saved!")
    st.rerun()
