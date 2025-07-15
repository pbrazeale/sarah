import streamlit as st
import os
from auth import show_auth_block
from functions.process_chapter import process_chapter

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
import_dir = "./working_dir/import"
os.makedirs(import_dir, exist_ok=True)

if uploaded_file is not None:
    save_path = os.path.join(import_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File saved to `{save_path}`")
    st.write("### File details")
    st.write(f"**Filename:** `{uploaded_file.name}`")
    st.write(f"**Size:** {round(len(uploaded_file.getbuffer()) / 1024, 2)} KB")
st.divider()

st.markdown("### 📜 Manuscripts")
docx_files = [f for f in os.listdir(import_dir) if f.endswith(".docx")]
if not docx_files:
    st.info("No manuscripts uploaded yet.")
else:
    for file in docx_files:
        st.markdown(f"- `{file}`")
st.divider()

st.markdown("### 🚀 Editing Process")
if st.button("🛠️ 1. Chapter Identification"):
    with st.spinner("Running SARAH's chapter processor..."):
        process_chapter()
    st.success("✅ Processing complete!")
st.divider()

st.markdown("### ✂️ Segments to Edit")
markdown_dir = "./working_dir/markdown"
os.makedirs(markdown_dir, exist_ok=True)
md_files = [f for f in os.listdir(markdown_dir) if f.endswith(".md")]
if not md_files:
    st.info('No segments generated yet. Run "🛠️ 1. Chapter Identification".')
else:
    for file in sorted(md_files):
        file_path = os.path.join(markdown_dir, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(f"📄 {file}"):
            st.code(content, language="markdown")
