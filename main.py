import streamlit as st

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="WatchVault | Premium Timepieces", page_icon="⌚", layout="wide")

# 2. Premium UI CSS Injection
st.markdown("""
    <style>
    /* Global Typography */
    h1, h2, h3, p, div {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #2D2323;
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #F5EBE6 0%, #EADBD4 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #EADBD4;
        margin-bottom: 3rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }
    .hero-title {
        color: #D9381E;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        color: #555555;
        font-size: 1.3rem;
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Feature Cards */
    .feature-card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #EADBD4;
        text-align: center;
        height: 100%;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-weight: 700;
        font-size: 1.2rem;
        color: #2D2323;
        margin-bottom: 0.5rem;
    }
    .feature-text {
        color: #666666;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding-top: 3rem;
        color: #888888;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "cart" not in st.session_state:
    st.session_state.cart = []

# 4. Hero Section
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">⌚ WatchVault</div>
    <div class="hero-subtitle">Discover our curated collection of luxury timepieces, designed for the modern connoisseur.</div>
</div>
""", unsafe_allow_html=True)

# 5. User Welcome / Call to Action
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.session_state.logged_in:
        st.success(f"**Welcome back, {st.session_state.username}!** Ready to find your next timepiece? Use the sidebar to explore.")
    else:
        st.info("👉 **Welcome!** Please go to the **Auth** tab in the sidebar to sign in and start shopping.", icon="👋")

st.markdown("<br><br>", unsafe_allow_html=True)

# 6. Feature Highlights (Styled as Cards)
c1, c2, c3, c4 = st.columns(4)

features = [
    {"icon": "🕐", "title": "Curated Collection", "desc": "From rugged tactical gear to fine Swiss-inspired dress watches."},
    {"icon": "🤖", "title": "AI Watch Expert", "desc": "Chat with our horology AI to find the perfect match for your lifestyle."},
    {"icon": "🔒", "title": "Secure Checkout", "desc": "Your data and orders are safely stored in our encrypted vault."},
    {"icon": "📦", "title": "Exclusive Models", "desc": "Shop limited editions like the Aureon and Italian hand-wound Virelli."}
]

columns = [c1, c2, c3, c4]

for col, feat in zip(columns, features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feat["icon"]}</div>
            <div class="feature-title">{feat["title"]}</div>
            <div class="feature-text">{feat["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)

# 7. Footer
st.markdown("""
<div class="footer">
    <hr style="border-top: 1px solid #EADBD4; margin-bottom: 1rem;">
    &copy; 2026 WatchVault Inc. | Powered by Streamlit & Supabase
</div>
""", unsafe_allow_html=True)