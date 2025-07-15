import streamlit as st
import os
import re
import json
from auth import show_auth_block
from functions.process_chapter import process_chapter
from functions.openrouter_call import call_openrouter

# login/logout
with st.sidebar:
    show_auth_block()
# Check authentication
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Import Title
st.title("📥 Upload")
st.markdown('''
### Upload a `.docx` file from your desktop for to **SARAH** begin analysis.
''', width="stretch",)
st.divider()


# === Display Manuscript Upload Section ===
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

param_file = os.path.join(import_dir, "parameters.json")
if os.path.exists(param_file):
    with open(param_file, "r", encoding="utf-8") as f:
        parameters = json.load(f)
else:
    parameters = {}

# Get the most recent full manuscript file
markdown_dir = "./working_dir/markdown"
os.makedirs(markdown_dir, exist_ok=True)
manuscripts = sorted([f for f in os.listdir(markdown_dir) if f.startswith("00_") and f.endswith(".md")])
manuscript_path = os.path.join(markdown_dir, manuscripts[0]) if manuscripts else None

# Editing paths (store in session if needed across buttons)
if "beat_sheet_path" not in st.session_state:
    st.session_state.beat_sheet_path = None
if "ms_dev_path" not in st.session_state:
    st.session_state.ms_dev_path = None


# # === Display Editing Process ===
# st.markdown("### 🚀 Editing Process")
# if st.button("🛠️ 1. Chapter Identification"):
#     with st.spinner("Running SARAH's chapter processor..."):
#         process_chapter()
#     st.success("✅ Chapter identification complete!")
#     st.rerun()

# if st.button("🧠 2. Beat Sheet Analysis"):
#     if not manuscript_path:
#         st.error("No manuscript found to analyze.")
#     else:
#         with st.spinner("Generating beat sheet..."):
#             beat_sheet_path = call_openrouter(
#                 objective_selection=0,
#                 manuscript_path=manuscript_path,
#                 parameters=parameters
#             )
#             st.session_state.beat_sheet_path = beat_sheet_path
#         st.success("✅ Beat sheet created.")

# if st.button("🧠 3. Full Manuscript Developmental Feedback"):
#     if not manuscript_path:
#         st.error("No manuscript file found.")
#     else:
#         with st.spinner("Running full manuscript developmental edit..."):
#             ms_dev_path = call_openrouter(
#                 objective_selection=1,
#                 manuscript_path=manuscript_path,
#                 parameters=parameters,
#                 beat_sheet_path=st.session_state.beat_sheet_path
#             )
#             st.session_state.ms_dev_path = ms_dev_path
#             try:
#                 os.remove(manuscript_path)
#                 st.info(f"🗑️ Removed: `{os.path.basename(manuscript_path)}`")
#             except Exception as e:
#                 st.warning(f"Failed to delete manuscript: {e}")
#         st.success("✅ Developmental feedback complete.")

# # CHAPTER EDITING
# chapter_files = sorted([f for f in os.listdir(markdown_dir) if f.startswith("Chapter") and f.endswith(".md")])
# next_chapter = chapter_files[0] if chapter_files else None

# if next_chapter:
#     next_chapter_path = os.path.join(markdown_dir, next_chapter)
#     if st.button(f"🧠 4. '{next_chapter}' Developmental Feedback"):
#         with st.spinner(f"Analyzing {next_chapter}..."):
#             _ = call_openrouter(
#                 objective_selection=1,
#                 manuscript_path=next_chapter_path,
#                 parameters=parameters,
#                 beat_sheet_path=st.session_state.beat_sheet_path,
#                 ms_developmental_edit_path=st.session_state.ms_dev_path
#             )
#             try:
#                 os.remove(next_chapter_path)
#                 st.info(f"🗑️ Removed: `{next_chapter}`")
#             except Exception as e:
#                 st.warning(f"Failed to delete chapter: {e}")
#         st.success(f"✅ Chapter feedback for '{next_chapter}' complete.")
# else:
#     st.info("No chapters found for analysis.")
# st.divider()


# # === Display Segments to Edit ===
# st.markdown("### ✂️ Segments to Edit")
# markdown_dir = "./working_dir/markdown"
# os.makedirs(markdown_dir, exist_ok=True)
# md_files = [f for f in os.listdir(markdown_dir) if f.endswith(".md")]
# if not md_files:
#     st.info('No segments generated yet. Run "🛠️ 1. Chapter Identification".')
# else:
#     for file in sorted(md_files):
#         file_path = os.path.join(markdown_dir, file)
#         with open(file_path, "r", encoding="utf-8") as f:
#             content = f.read()
#         with st.expander(f"📄 {file}"):
#             st.code(content, language="markdown")
