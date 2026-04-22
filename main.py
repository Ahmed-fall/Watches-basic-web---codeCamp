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

# 2. DEFINING THE NAVIGATION
# This centralizes control and prevents recursion loops
pg = st.navigation([
    st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/Auth.py", title="Sign In / Sign Up", icon="🔐"),
    st.Page("pages/Explore_Watches.py", title="Explore Watches", icon="🕐"),
    st.Page("pages/Shopping_Cart.py", title="Shopping Cart", icon="🛒"),
    st.Page("pages/AI_Watch_Expert.py", title="AI Expert", icon="🤖"),
])

# 3. BACKGROUND & GLOBAL UI STYLING
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        st.markdown(f"""
        <style>
        /* Target the app view container so the header stays on top */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Fix the Sidebar Overlay for Mobile */
        [data-testid="stSidebar"] {{
            background-color: rgba(14, 17, 23, 0.95) !important;
            backdrop-filter: blur(10px);
        }}

        /* Header Layering - Force it to sit above the background */
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
            z-index: 1000000 !important;
            display: flex !important;
            visibility: visible !important;
        }}

        /* HIGH-VISIBILITY GOLD MENU BUTTON */
        [data-testid="stHeader"] button {{
            background-color: #D4AF37 !important;
            color: black !important;
            border-radius: 50% !important;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.6) !important;
            width: 45px !important;
            height: 45px !important;
            margin-left: 15px !important;
            visibility: visible !important;
            opacity: 1 !important;
        }}

        /* NAVIGATION LINKS STYLING */
        [data-testid="stSidebarNav"] {{
            padding-top: 2rem;
        }}

        /* MOBILE RESPONSIVENESS */
        @media (max-width: 768px) {{
            [data-testid="stSidebar"] {{
                width: 70vw !important;
            }}
            .block-container {{
                padding-top: 4rem !important;
            }}
        }}

        /* Hide standard Streamlit decorations */
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Background image not found at {image_path}")

# Execute background injection
set_background(os.path.join("images", "9.jpg"))

# 4. RUN NAVIGATION
# This renders the selected page from your 'pages/' folder
pg.run()