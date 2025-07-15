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

# Export Title
st.title("📤 Download")
st.markdown('''
### Downlaod **SARAH**'s developmental edits and story analysis.
''', width="stretch",)
st.divider()

# Export directory
export_dir = "./working_dir/export"
os.makedirs(export_dir, exist_ok=True)

# List files
files = sorted([
    f for f in os.listdir(export_dir)
    if os.path.isfile(os.path.join(export_dir, f))
])

if not files:
    st.info("📂 No files found in export folder.")
else:
    st.markdown("### 🗂️ Files Available for Download")

    # Track selection in session state
    if "selected_export_file" not in st.session_state:
        st.session_state.selected_export_file = None

    for file in files:
        file_path = os.path.join(export_dir, file)

        with st.container(border=True):
            col1, col2 = st.columns([8, 2])
            with col1:
                st.write(f"📄 `{file}`")
            with col2:
                if st.button("⬇️ Download", key=file):
                    with open(file_path, "rb") as f:
                        file_bytes = f.read()
                    st.download_button(
                        label=f"Download {file}",
                        data=file_bytes,
                        file_name=file,
                        mime="application/octet-stream",
                        key=f"download_{file}"
                    )