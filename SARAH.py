import streamlit as st
from auth import show_auth_block

st.set_page_config(page_title="SARAH", layout="wide")

st.sidebar.success("Start Editing")

# login/logout
with st.sidebar:
    show_auth_block()

# HERO SECTION
st.html(
    """
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="font-size: 3rem;">🧠 SARAH</h1>
        <h3 style="color: #6c757d;">Story Analysis & Revision AI Helper</h3>
        <p style="max-width: 700px; margin: auto; font-size: 1.2rem; text-align: justify;">
            <b>Sarah</b> is an AI-powered <b>developmental edititor</b> designed to assist authors to refine their manuscripts, with professional-grade insights, and support your storytelling and publishing goals.
        </p>
        <br>
    </div>
    """
)
st.divider()

# FEATURE SECTION
st.markdown("### What SARAH Can Do For You")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### 🛠️ Structure Analysis")
    st.markdown("Get beat sheet analysis and narrative flow evaluation.")
with col2:
    st.markdown("#### 📝 Line Editing")
    st.markdown("Receive grammar, clarity, and style suggestions by chapter.")
with col3:
    st.markdown("#### 🧑‍🤝‍🧑 Character & Theme Feedback")
    st.markdown("Deep analysis of arcs, motivation, and consistency.")
st.divider()

# CTA: WAITLIST SIGNUP FORM
st.markdown("### 🚀 Join the Early Access List")
st.markdown(
    """
    SARAH is currently in early development. 
    
    Join the waitlist and be among the first to access her full suite of tools.
    """
)
with st.form("waitlist_form"):
    email = st.text_input("Enter your email to join the waitlist:")
    submitted = st.form_submit_button("✅ Join Waitlist")
    if submitted:
        if "waitlist" not in st.session_state:
            st.session_state.waitlist = []
        st.session_state.waitlist.append(email)
        st.success("You're on the list! We'll let you know when SARAH launches.")
st.divider()

# FOOTER / TAGLINE
st.html(
    """
    <div style="text-align: center; color: #aaa; font-size: 0.9rem; margin-top: 2rem;">
        © 2025 SARAH: Story Analysis & Revision AI Helper
    </div>
    """
)
