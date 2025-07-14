import streamlit as st
import os
from auth import show_auth_block

# login/logout
with st.sidebar:
    show_auth_block()
# Check authentication
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Import Title
st.title("📥 Import")
st.markdown('''
### Upload a `.docx` file from your desktop for to **SARAH** begin analysis.
''', width="stretch",)
st.divider()

# Upload
uploaded_file = st.file_uploader("Choose a `.docx` file", type=["docx"])

save_dir = "./working_dir/import"
os.makedirs(save_dir, exist_ok=True)

if uploaded_file is not None:
    save_path = os.path.join(save_dir, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ File saved to `{save_path}`")
    st.write("### File details")
    st.write(f"**Filename:** `{uploaded_file.name}`")
    st.write(f"**Size:** {round(len(uploaded_file.getbuffer()) / 1024, 2)} KB")
