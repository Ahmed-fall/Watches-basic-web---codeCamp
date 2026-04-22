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
# We point 'Home' to the new file in the pages folder to avoid the loop
pg = st.navigation([
    st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/Auth.py", title="Sign In / Sign Up", icon="🔐"),
    st.Page("pages/Explore_Watches.py", title="Explore Watches", icon="🕐"),
    st.Page("pages/Shopping_Cart.py", title="Shopping Cart", icon="🛒"),
    st.Page("pages/AI_Watch_Expert.py", title="AI Expert", icon="🤖"),
])

# 3. BACKGROUND INJECTION (Stays here so it applies to every page)
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover; background-position: center; background-attachment: fixed;
        }}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

set_background(os.path.join("images", "9.jpg"))

st.markdown("""
    <style>
    /* 1. Hide the collapse/close button on Desktop & Mobile */
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }

    /* 2. Target the mobile-specific 'Sidebar' overlay trigger */
    button[aria-label="Open sidebar"] {
        display: none !important;
    }

    /* 3. Mobile specific adjustment: Ensure the sidebar doesn't 
       auto-collapse when a user taps a link */
    @media (max-width: 768px) {
        /* This keeps the sidebar container visible on smaller screens */
        [data-testid="stSidebar"] {
            left: 0 !important;
            position: relative !important;
        }
        
        /* Forces the main content to wait for the sidebar */
        .main {
            margin-left: 0 !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 4. RUN NAVIGATION
pg.run()