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
    /* target the sidebar container */
    [data-testid="stSidebar"] {
        transition: width 0.3s ease;
    }

    /* MOBILE SPECIFIC RULES (Screens smaller than 768px) */
    @media (max-width: 768px) {
        /* Reduce sidebar width to 60% of the screen instead of 90% */
        [data-testid="stSidebar"] {
            width: 65vw !important;
            min-width: 65vw !important;
        }

        /* Shrink the navigation text a bit so it fits in the narrower bar */
        [data-testid="stSidebar"] div[role="navigation"] {
            font-size: 0.85rem !important;
        }

        /* Adjust the background image positioning so it doesn't look weird when squeezed */
        .stApp {
            background-position: 70% center !important;
        }
    }

    /* TABLET SPECIFIC RULES (Optional) */
    @media (min-width: 769px) and (max-width: 1024px) {
        [data-testid="stSidebar"] {
            width: 300px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 4. RUN NAVIGATION
pg.run()