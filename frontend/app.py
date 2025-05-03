import streamlit as st

st.set_page_config(page_title="AI Troubleshooter", page_icon="🤖", layout="centered")

from libs.auth import check_auth, login, is_logged_in
from libs.chat import chat


# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Authentication check
check_auth()

# Route
if is_logged_in():
    chat()
else:
    login()
