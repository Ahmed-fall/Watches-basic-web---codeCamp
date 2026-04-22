import streamlit as st

st.markdown("""
    <style>
    .hero-container {
        background: linear-gradient(180deg, rgba(14, 17, 23, 0.85) 0%, rgba(14, 17, 23, 0.6) 100%);
        padding: 4rem 2rem; border-radius: 12px; text-align: center;
        border: 1px solid rgba(212, 175, 55, 0.2); backdrop-filter: blur(8px);
    }
    .hero-title { color: #D4AF37; font-size: 4rem; font-weight: 700; text-transform: uppercase; }
    .premium-card {
        background: rgba(20, 22, 28, 0.85); border-top: 3px solid #D4AF37;
        padding: 2.5rem 1.5rem; border-radius: 8px; text-align: center; height: 100%;
    }
    </style>
    
    <div class="hero-container">
        <div class="hero-title">WatchVault</div>
        <div style="color: #F0F2F6; font-size: 1.3rem;">Curated luxury timepieces for the modern connoisseur.</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
features = [
    {"icon": "🕰️", "title": "Curated", "desc": "Fine Swiss-inspired watches."},
    {"icon": "🤖", "title": "AI Expert", "desc": "Consult our horology AI."},
    {"icon": "🛡️", "title": "Secure", "desc": "Encrypted data storage."},
    {"icon": "💎", "title": "Exclusive", "desc": "Limited editions."}
]

for col, feat in zip([c1, c2, c3, c4], features):
    with col:
        st.markdown(f"""
        <div class="premium-card">
            <div style="font-size: 2.8rem;">{feat["icon"]}</div>
            <div style="color: #D4AF37; font-weight: bold;">{feat["title"]}</div>
            <div style="color: #D1D5DB;">{feat["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* This hides the 'X' button inside the sidebar and the '>' button on the main page */
    [data-testid="stSidebarCollapseButton"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)