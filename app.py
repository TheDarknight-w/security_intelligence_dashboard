# app.py
import streamlit as st
from api import check_pwned, check_url
from utils import check_strength, generate_secure_password
from db import check_login, save_history, create_default_user, get_history

create_default_user()

st.set_page_config(page_title="Cyber Guard Pro", page_icon="🛡️", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login to Cyber Guard")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(user, pwd):
            st.session_state.logged_in = True
            st.session_state.user = user
            st.rerun()
        else:
            st.error("Invalid credentials")
else:
    st.sidebar.title(f"👤 {st.session_state.user}")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🛡️ Security Intelligence Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["Password Auditor", "URL Scanner", "Password Generator"])

    with tab1:
        st.subheader("Breach Analysis")
        p_input = st.text_input("Test a password", type="password")
        if st.button("Analyze"):
            strength = check_strength(p_input)
            pwned = check_pwned(p_input)
            save_history(st.session_state.user, "Pass Audit", f"{strength} | {pwned}")
            st.metric("Strength", strength)
            if "Leaked" in pwned: st.error(pwned)
            else: st.success(pwned)

    with tab2:
        st.subheader("VirusTotal Scanner")
        u_input = st.text_input("URL to scan")
        if st.button("Scan URL"):
            with st.spinner("Scanning..."):
                res = check_url(u_input)
                save_history(st.session_state.user, u_input, res)
                st.info(f"Report: {res}")

    with tab3:
        st.subheader("Secure Generator")
        length = st.slider("Length", 8, 32, 16)
        if st.button("Generate"):
            new_pass = generate_secure_password(length)
            st.code(new_pass)
            st.toast("Generated!")

    st.divider()
    with st.expander("Recent Activity"):
        history = get_history(st.session_state.user)
        if history: st.table(history)