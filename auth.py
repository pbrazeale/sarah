# auth.py
import streamlit as st

USERS = {
    "test@test.com": "test123",
    "admin@example.com": "adminpass"
}

def show_auth_block():
    st.markdown("### 🔐 Login/Logout")
    if st.session_state.get("logged_in", False):
        st.markdown(f"👤 {st.session_state.get('user_email', '')}")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.rerun()
    else:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                if email in USERS and USERS[email] == password:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.success(f"Welcome, {email}!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
