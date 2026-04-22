import os
import base64
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="WatchVault | Luxury Timepieces", 
    page_icon="⌚", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 2. NAVIGATION DEFINITION
pg = st.navigation([
    st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/Auth.py", title="Sign In / Sign Up", icon="🔐"),
    st.Page("pages/Explore_Watches.py", title="Explore Watches", icon="🕐"),
    st.Page("pages/Shopping_Cart.py", title="Shopping Cart", icon="🛒"),
    st.Page("pages/AI_Watch_Expert.py", title="AI Expert", icon="🤖"),
])

# 3. GLOBAL LUXURY STYLING
def apply_elegant_styles(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        st.markdown(f"""
        <style>
        /* Layer 1: The Background Image */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Layer 2: Overlay for better contrast across the whole app */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(0, 0, 0, 0.4); /* Darkens the image slightly */
            z-index: 0;
        }}

        /* Elegant Sidebar: Semi-Black Glass */
        [data-testid="stSidebar"] {{
            background-color: rgba(5, 5, 5, 0.85) !important;
            backdrop-filter: blur(15px) !important;
            border-right: 1px solid rgba(212, 175, 55, 0.3) !important;
        }}

        /* Floating Gold Menu Button (Fixed Layering) */
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
            z-index: 1000001 !important;
        }}

        [data-testid="stHeader"] button {{
            background-color: #000000 !important; /* Pure Black button */
            color: #D4AF37 !important; /* Gold Icon */
            border: 1px solid #D4AF37 !important;
            border-radius: 50% !important;
            box-shadow: 0 0 10px rgba(212, 175, 55, 0.4) !important;
            width: 45px !important;
            height: 45px !important;
        }}

        /* Content Area Padding */
        .block-container {{
            padding-top: 5rem !important;
            z-index: 1;
        }}

        /* Hide Streamlit elements */
        footer {{visibility: hidden;}}
        header {{visibility: visible !important;}}
        </style>
        """, unsafe_allow_html=True)

apply_elegant_styles(os.path.join("images", "9.jpg"))

pg.run()