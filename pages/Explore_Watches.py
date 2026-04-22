import os
import base64
import streamlit as st
from supabase import create_client, Client

# 1. Page Config
st.set_page_config(page_title="Collection | WatchVault", page_icon="🕐", layout="wide")

# 2. Database Connection Fix
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# 3. Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
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

# 5. Premium Scoped CSS for the Collection
st.markdown("""
    <style>
    /* Header Styling */
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
        color: #D4AF37;
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
    
    /* Warning Styling */
    .auth-warning {
        background: rgba(30, 30, 36, 0.95);
        border-left: 4px solid #D4AF37;
        padding: 2rem;
        border-radius: 6px;
        text-align: center;
        font-size: 1.2rem;
        color: #FAFAFA;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-top: 2rem;
        backdrop-filter: blur(5px);
    }

    /* Watch Card Typography (Dark Mode Adapted) */
    .watch-brand { 
        font-size: 1.1rem; 
        font-weight: 700; 
        color: #D4AF37; /* Changed to Gold */
        margin-bottom: -5px; 
        letter-spacing: 1px;
    }
    .watch-model { 
        font-size: 1.4rem; 
        font-weight: 600; 
        color: #FFFFFF; /* Changed to White */
        margin-bottom: 5px;
    }
    .watch-price { 
        font-size: 1.4rem; 
        font-weight: 700; 
        color: #D4AF37; 
        margin-top: 10px; 
        margin-bottom: 10px;
    }
    .watch-desc { 
        color: #D1D5DB; /* Changed to Light Gray */
        font-size: 0.95rem; 
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

# 6. Header UI
st.markdown("""
<div class="page-title-container">
    <div class="page-title">🕐 Explore Collection</div>
    <div class="page-subtitle">Find the perfect addition to your personal vault.</div>
</div>
""", unsafe_allow_html=True)

# 7. Authentication Check
if not st.session_state.get("logged_in"):
    st.markdown("""
    <div class="auth-warning">
        Please sign in via the <b>Auth</b> menu to shop the collection.
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# 8. Filters
with st.container(border=True):
    st.markdown("### Filter Collection")
    col1, col2 = st.columns(2)
    with col1:
        movement_filter = st.selectbox("Filter by Movement", ["All", "Quartz", "Automatic", "Mechanical"])
    with col2:
        max_price = st.slider("Max Price ($)", 100, 6000, 6000, step=100)

st.markdown("<br>", unsafe_allow_html=True)

# 9. Fetch watches from Database
try:
    query = supabase.table("watches").select("*")
    result = query.execute()
    watches = result.data
except Exception as e:
    st.error(f"Failed to load collection from database: {e}")
    st.stop()

# Apply filters
if movement_filter != "All":
    watches = [w for w in watches if w["movement_type"] == movement_filter]
watches = [w for w in watches if w["price"] <= max_price]

if not watches:
    st.info("No watches match your current filters.")
    st.stop()

# 10. Display in grid (3 columns)
cols = st.columns(3)
for i, watch in enumerate(watches):
    with cols[i % 3]:
        # Utilizing Streamlit's native container for a clean card border
        with st.container(border=True):
            img_path = os.path.join("images", watch["image_filename"])
            
            # Display Image if it exists
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning("Image missing")
            
            # Premium HTML Formatting
            st.markdown(f"<div class='watch-brand'>{watch['brand'].upper()}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='watch-model'>{watch['model']}</div>", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#A0AEC0; font-size: 0.9rem;'><i>{watch['movement_type']}</i></span>", unsafe_allow_html=True)
            st.markdown(f"<div class='watch-price'>${watch['price']:,.2f}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='watch-desc'>{watch['description']}</div><br>", unsafe_allow_html=True)

            if watch["stock_quantity"] > 0:
                if st.button("Add to Cart", key=f"cart_{watch['watch_id']}", use_container_width=True):
                    st.session_state.cart.append({
                        "watch_id":  watch["watch_id"],
                        "brand":     watch["brand"],
                        "model":     watch["model"],
                        "price":     watch["price"],
                        "image":     watch["image_filename"]
                    })
                    # Swapped standard success for a toast so it doesn't disrupt the UI grid
                    st.toast(f"Added {watch['model']} to cart! 🛒") 
            else:
                st.error("Out of Stock")