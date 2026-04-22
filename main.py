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
    /* This hides the 'X' button inside the sidebar and the '>' button on the main page */
    [data-testid="stSidebarCollapseButton"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# 4. RUN NAVIGATION
pg.run()