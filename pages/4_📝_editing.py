import streamlit as st
import os
import re
import json
import shutil
from auth import show_auth_block
from functions.process_chapter import process_chapter
from functions.openrouter_call import call_openrouter

# login/logout
with st.sidebar:
    show_auth_block()
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Setup paths
import_dir = "./working_dir/import"
markdown_dir = "./working_dir/markdown"
export_dir = "./working_dir/export"
os.makedirs(import_dir, exist_ok=True)
os.makedirs(markdown_dir, exist_ok=True)
os.makedirs(export_dir, exist_ok=True)

# === HELPER FUNCTIONS ===
def detect_existing_beat_sheet():
    for fname in os.listdir(export_dir):
        if fname.startswith("Beat_Sheet_") and fname.endswith(".md"):
            return os.path.join(export_dir, fname)
    return None

def detect_existing_dev_edit():
    for fname in os.listdir(export_dir):
        if fname.startswith("MS_Dev_Edit_") and fname.endswith(".md"):
            return os.path.join(export_dir, fname)
    return None

# Load parameters
param_file = os.path.join(import_dir, "parameters.json")
if os.path.exists(param_file):
    with open(param_file, "r", encoding="utf-8") as f:
        parameters = json.load(f)
else:
    parameters = {}

# === STATE DETECTION ===
chapter_files = sorted([f for f in os.listdir(markdown_dir) if f.startswith("Chapter") and f.endswith(".md")])
st.session_state.chapters_identified = bool(chapter_files)
st.session_state.beat_sheet_path = detect_existing_beat_sheet()
st.session_state.ms_dev_edit_path = detect_existing_dev_edit()

manuscripts = sorted([f for f in os.listdir(markdown_dir) if f.startswith("00_") and f.endswith(".md")])
manuscript_path = os.path.join(markdown_dir, manuscripts[0]) if manuscripts else None

# Import Title
st.title("📝 Editing")
st.markdown("### Let **SARAH** begin the developmental editing process.")
st.divider()

# # === System Testing to clear Start New Manuscript===
# if st.button("🧹 Start New Manuscript"):
#     keys_to_clear = ["chapters_identified", "beat_sheet_path", "ms_dev_edit_path"]
#     for key in keys_to_clear:
#         if key in st.session_state:
#             del st.session_state[key]
    
#     # Clear generated files from markdown and export directories
#     for f in os.listdir(markdown_dir):
#         if f.startswith("Chapter") or f.startswith("00_"):
#             os.remove(os.path.join(markdown_dir, f))
#     for f in os.listdir(export_dir):
#          os.remove(os.path.join(export_dir, f))

#     st.success("State and generated files cleared. Ready for a new manuscript.")
#     st.rerun()


# === Editing Process ===
st.markdown("### 🚀 Editing Process")

# 1. Chapter Identification
if st.session_state.chapters_identified:
    st.success(f"✅ Chapters already identified ({len(chapter_files)} found).")
else:
    if st.button("🛠️ 1. Chapter Identification"):
        with st.spinner("Running SARAH's chapter processor..."):
            process_chapter() 
        st.success("✅ Chapter identification complete!")
        st.rerun()

# 2. Beat Sheet Analysis
if st.session_state.beat_sheet_path:
    st.success(f"✅ Beat sheet already exists: `{os.path.basename(st.session_state.beat_sheet_path)}`")
else:
    if st.button("🧠 2. Beat Sheet Analysis", disabled=not st.session_state.chapters_identified):
        if not manuscript_path:
            st.error("No manuscript found to analyze. Please ensure '1. Chapter Identification' has been run successfully.")
        else:
            with st.spinner("Generating beat sheet..."):
                call_openrouter(
                    objective_selection=0,
                    manuscript_path=manuscript_path,
                    parameters=parameters
                )
            st.success("✅ Beat sheet created.")
            st.rerun()

# 3. Full Manuscript Developmental Feedback
if st.session_state.ms_dev_edit_path:
    st.success(f"✅ Developmental feedback already exists: `{os.path.basename(st.session_state.ms_dev_edit_path)}`")
else:
    button_disabled = not st.session_state.beat_sheet_path
    if st.button("🧠 3. Full Manuscript Developmental Feedback", disabled=button_disabled):
        if not manuscript_path:
            st.error("No manuscript file found.")
        else:
            with st.spinner("Running full manuscript developmental edit..."):
                call_openrouter(
                    objective_selection=1,
                    manuscript_path=manuscript_path,
                    parameters=parameters,
                    beat_sheet_path=st.session_state.beat_sheet_path
                )
                try:
                    os.remove(manuscript_path)
                    st.info(f"🗑️ Removed: `{os.path.basename(manuscript_path)}`")
                except Exception as e:
                    st.warning(f"Failed to delete manuscript: {e}")
            st.success("✅ Developmental feedback complete.")
            st.rerun()

# 4. Chapter Feedback
chapter_files = sorted([f for f in os.listdir(markdown_dir) if f.startswith("Chapter") and f.endswith(".md")])
next_chapter = chapter_files[0] if chapter_files else None

if next_chapter:
    next_chapter_path = os.path.join(markdown_dir, next_chapter)
    button_disabled = not st.session_state.ms_dev_edit_path
    if st.button(f"🧠 4. '{next_chapter}' Developmental Feedback", disabled=button_disabled):
        with st.spinner(f"Analyzing {next_chapter}..."):
            call_openrouter(
                objective_selection=2,
                manuscript_path=next_chapter_path,
                parameters=parameters,
                beat_sheet_path=st.session_state.beat_sheet_path,
                ms_developmental_edit_path=st.session_state.ms_dev_edit_path
            )
            try:
                os.remove(next_chapter_path)
                st.info(f"🗑️ Removed: `{next_chapter}`")
            except Exception as e:
                st.warning(f"Failed to delete chapter: {e}")
        st.success(f"✅ Chapter feedback for '{next_chapter}' complete.")
        st.rerun()
else:
    if st.session_state.chapters_identified and st.session_state.ms_dev_edit_path:
        st.success("✅ All chapters have been analyzed.")

# === Display Segments to Edit ===
st.markdown("### ✂️ Segments to Edit")
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
