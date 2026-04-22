import streamlit as st

st.markdown("""
    <style>
    /* Hero Section with high-contrast gradient */
    .hero-container {
        background: linear-gradient(135deg, rgba(0,0,0,0.95) 0%, rgba(20,20,20,0.7) 100%);
        padding: 5rem 2rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(212, 175, 55, 0.4);
        backdrop-filter: blur(10px);
        margin-bottom: 3rem;
    }
    .hero-title {
        color: #D4AF37;
        font-size: clamp(2.5rem, 8vw, 4.5rem); /* Responsive font size */
        font-weight: 800;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        color: #FFFFFF;
        font-size: 1.2rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    /* Feature Cards: Deep Black with Gold Border */
    .premium-card {
        background: rgba(5, 5, 5, 0.9) !important;
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 2.5rem 1.5rem;
        border-radius: 12px;
        text-align: center;
        height: 100%;
        transition: all 0.3s ease;
    }
    .premium-card:hover {
        border-color: #D4AF37;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.6);
    }
    </style>
    
    <div class="hero-container">
        <div class="hero-title">WatchVault</div>
        <div class="hero-subtitle">PRECISION • HERITAGE • LUXURY</div>
    </div>
""", unsafe_allow_html=True)

cols = st.columns(4)
features = [
    {"icon": "🕰️", "title": "Curated", "desc": "Swiss-engineered excellence."},
    {"icon": "🤖", "title": "AI Expert", "desc": "Personal horology consultant."},
    {"icon": "🛡️", "title": "Secure", "desc": "Encrypted digital ownership."},
    {"icon": "💎", "title": "Exclusive", "desc": "Rare boutique limited editions."}
]

for col, feat in zip(cols, features):
    with col:
        st.markdown(f"""
        <div class="premium-card">
            <div style="font-size: 3rem; margin-bottom: 15px;">{feat["icon"]}</div>
            <div style="color: #D4AF37; font-weight: bold; letter-spacing: 1px;">{feat["title"]}</div>
            <div style="color: #BBBBBB; font-size: 0.9rem; margin-top: 10px; line-height: 1.5;">{feat["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)