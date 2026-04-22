import streamlit as st
import bcrypt
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

st.title("🔐 Account Access")

# Center the auth forms
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    tab1, tab2 = st.tabs(["Sign In", "Create Account"])

    # ---------- SIGN IN ----------
    with tab1:
        with st.container(border=True):
            st.subheader("Welcome Back")
            username = st.text_input("Username", key="si_user")
            password = st.text_input("Password", type="password", key="si_pass")
            
            if st.button("Sign In", use_container_width=True, type="primary"):
                result = supabase.table("users").select("*").eq("username", username).execute()
                if result.data:
                    user = result.data[0]
                    if bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
                        st.session_state.logged_in = True
                        st.session_state.username  = user["username"]
                        st.session_state.user_id   = user["user_id"]
                        st.success(f"Welcome, {username}!")
                        st.rerun()
                    else:
                        st.error("Incorrect password.")
                else:
                    st.error("User not found.")

    # ---------- SIGN UP ----------
    with tab2:
        with st.container(border=True):
            st.subheader("Join WatchVault")
            new_username = st.text_input("Username", key="su_user")
            new_email    = st.text_input("Email", key="su_email")
            new_password = st.text_input("Password", type="password", key="su_pass")
            
            if st.button("Sign Up", use_container_width=True):
                if not new_username or not new_email or not new_password:
                    st.error("All fields are required.")
                else:
                    hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
                    try:
                        supabase.table("users").insert({
                            "username": new_username,
                            "email": new_email,
                            "password_hash": hashed
                        }).execute()
                        st.success("Account created! Go to Sign In.")
                    except Exception as e:
                        st.error(f"Error: {e}")

    if st.session_state.logged_in:
        st.markdown("---")
        if st.button("Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username  = None
            st.session_state.user_id   = None
            st.session_state.cart      = []
            st.rerun()