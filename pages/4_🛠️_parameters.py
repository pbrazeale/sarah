import streamlit as st

st.set_page_config(page_title="Parameters", layout="wide")

st.title("Parameters")

# --- Point of View ---
st.subheader("1. Point of View")
pov = st.radio("Choose the narrative perspective:", [
    "1st Person",
    "Limited 3rd Person",
    "Omniscient 3rd Person"
], horizontal=True)

# --- Tense ---
st.subheader("2. Tense")
tense = st.radio("Choose the tense of narration:", [
    "Present",
    "Past"
], horizontal=True)

# --- Genre Selection ---
st.subheader("3. Genre Selection")

genre_options = {
    "Romance": [
        "Contemporary",
        "Historical",
        "Paranormal",
        "Romantic Comedy"
    ],
    "Mystery": [
        "Cozy",
        "Detective",
        "Noir",
        "Paranormal"
    ],
    "Thriller": [
        "Psychological",
        "Political",
        "Action",
        "Crime",
        "Legal"
    ],
    "Science Fiction": [],
    "Fantasy": [
        "Epic",
        "Urban",
        "Sword & Sorcery"
    ],
    "Horror": []
}

# Primary genre selection
primary_genre = st.selectbox("Primary Genre:", list(genre_options.keys()))

# Sub-genre selection (only if available)
sub_genre = None
if genre_options[primary_genre]:
    sub_genre = st.selectbox("Sub-Genre:", genre_options[primary_genre])

# --- Main Character ---
st.subheader("4. Main Character")
main_character = st.text_input("Main Character Name:")

# --- Display Summary (optional) ---
st.markdown("### 🧾 Summary")
st.write(f"**Point of View:** {pov}")
st.write(f"**Tense:** {tense}")
st.write(f"**Genre:** {primary_genre}" + (f" > {sub_genre}" if sub_genre else ""))
st.write(f"**Main Character:** {main_character}")
