import os
import base64
import bcrypt
import streamlit as st
from supabase import create_client, Client

# 1. Page Config
st.set_page_config(page_title="Auth | WatchVault", page_icon="🔐", layout="wide")

# 2. Database Connection Fix
# We securely load the credentials and build the Supabase client
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# 3. Session State Initialization
# Prevents errors if a user visits this page first
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "cart" not in st.session_state:
    st.session_state.cart = []

# 4. Background Image Injection
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

set_background(os.path.join("images", "9.jpg"))

# 5. Premium Scoped CSS
st.markdown("""
    <style>
    .page-title-container {
        background: rgba(14, 17, 23, 0.85);
        padding: 2rem 2rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid rgba(212, 175, 55, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 2.5rem;
        backdrop-filter: blur(8px);
    }
    .page-title {
        color: #D4AF37; /* Rich Gold */
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        font-family: 'Georgia', serif;
    }
    .page-subtitle {
        color: #F0F2F6;
        font-size: 1.1rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# 6. Header UI
st.markdown("""
<div class="page-title-container">
    <div class="page-title">🔐 Vault Access</div>
    <div class="page-subtitle">Sign in or create an account to secure your timepieces.</div>
</div>
""", unsafe_allow_html=True)

# 7. Authentication Forms
# Center the auth forms
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.logged_in:
        with st.container(border=True):
            st.subheader("Account Status")
            st.success(f"You are securely signed in as **{st.session_state.username}**.")
            st.markdown("---")
            if st.button("Sign Out", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username  = None
                st.session_state.user_id   = None
                st.session_state.cart      = []
                st.rerun()
    else:
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