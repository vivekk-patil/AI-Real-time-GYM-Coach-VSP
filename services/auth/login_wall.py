import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("🏋️‍♂️ AI Real-time GYM Trainer - VSP")
    st.markdown("### Welcome! Please enter a username to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="unique name e.g. Vivekpatil")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        user = get_or_create_user(username)
    
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.rerun()

    st.markdown("""
    <footer style="
        text-align: center;
        padding: 15px;
        margin-top: 20px;
        border-top: 1px solid #ddd;
        color: white;
        font-size: 14px;
    ">
        © 2026 AI Real-time GYM Coach | Developed by Vivek Satish Patil
    </footer>
    """, unsafe_allow_html=True)

    return False