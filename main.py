import os
import base64
import streamlit as st

# 1. Page Config
st.set_page_config(page_title="WatchVault | Luxury Timepieces", page_icon="⌚", layout="wide")

# 2. Background Image Injection
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
        /* Push content up slightly */
        .block-container {{
            padding-top: 3rem;
            padding-bottom: 2rem;
        }}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Background image not found at {image_path}")

set_background(os.path.join("images", "9.jpg"))

# 3. Premium Scoped CSS (No Global Tags to Protect the Sidebar)
st.markdown("""
    <style>
    /* Hero Banner */
    .hero-container {
        background: linear-gradient(180deg, rgba(14, 17, 23, 0.85) 0%, rgba(14, 17, 23, 0.6) 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid rgba(212, 175, 55, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 2.5rem;
        backdrop-filter: blur(8px);
    }
    .hero-title {
        color: #D4AF37; /* Rich Gold */
        font-size: 4rem;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        font-family: 'Georgia', serif;
    }
    .hero-subtitle {
        color: #F0F2F6;
        font-size: 1.3rem;
        font-weight: 300;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
        letter-spacing: 1px;
    }
    
    /* Welcome / Login Status Bar */
    .status-bar {
        background: rgba(30, 30, 36, 0.9);
        border-left: 4px solid #D4AF37;
        padding: 1rem 1.5rem;
        border-radius: 6px;
        margin-bottom: 3rem;
        font-size: 1.1rem;
        color: #FAFAFA;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .status-highlight {
        color: #D4AF37;
        font-weight: bold;
    }

    /* Premium Feature Cards */
    .premium-card {
        background: rgba(20, 22, 28, 0.85);
        border-top: 3px solid #D4AF37;
        padding: 2.5rem 1.5rem;
        border-radius: 8px;
        text-align: center;
        height: 100%;
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
        transition: transform 0.3s ease, background 0.3s ease;
        backdrop-filter: blur(5px);
    }
    .premium-card:hover {
        transform: translateY(-8px);
        background: rgba(30, 32, 40, 0.95);
    }
    .card-icon {
        font-size: 2.8rem;
        margin-bottom: 1rem;
    }
    .card-title {
        color: #D4AF37;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .card-desc {
        color: #D1D5DB;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Session State Init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# 5. Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">WatchVault</div>
    <div class="hero-subtitle">Discover our curated collection of luxury timepieces. Engineered for precision, designed for the modern connoisseur.</div>
</div>
""", unsafe_allow_html=True)

# 6. Status Bar
if st.session_state.logged_in:
    st.markdown(f"""
    <div class="status-bar">
        Welcome back, <span class="status-highlight">{st.session_state.username}</span>. Use the sidebar to explore the collection.
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="status-bar">
        Access your account via the <span class="status-highlight">Auth</span> menu in the sidebar to begin your journey.
    </div>
    """, unsafe_allow_html=True)

# 7. Feature Grid
c1, c2, c3, c4 = st.columns(4)

features = [
    {"icon": "🕰️", "title": "Curated", "desc": "From rugged tactical gear to fine Swiss-inspired dress watches."},
    {"icon": "🤖", "title": "AI Expert", "desc": "Consult our horology AI to find the perfect match for your lifestyle."},
    {"icon": "🛡️", "title": "Secure", "desc": "Your data and orders are safely stored in our encrypted vault."},
    {"icon": "💎", "title": "Exclusive", "desc": "Shop limited editions and Italian hand-wound masterpieces."}
]

for col, feat in zip([c1, c2, c3, c4], features):
    with col:
        st.markdown(f"""
        <div class="premium-card">
            <div class="card-icon">{feat["icon"]}</div>
            <div class="card-title">{feat["title"]}</div>
            <div class="card-desc">{feat["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)