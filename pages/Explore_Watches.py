import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Premium UI CSS Injection
st.markdown("""
    <style>
    .watch-brand { font-size: 1.1rem; font-weight: 700; color: #D9381E; margin-bottom: -10px; }
    .watch-model { font-size: 1.3rem; font-weight: 600; color: #2D2323; }
    .watch-price { font-size: 1.4rem; font-weight: 700; color: #2D2323; margin-top: 10px; }
    .watch-desc { color: #555555; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🕐 Explore Collection")

if not st.session_state.get("logged_in"):
    st.warning("Please sign in to shop.")
    st.stop()

# Filters
st.markdown("### Filter Collection")
col1, col2 = st.columns(2)
with col1:
    movement_filter = st.selectbox("Filter by Movement", ["All", "Quartz", "Automatic", "Mechanical"])
with col2:
    max_price = st.slider("Max Price ($)", 100, 6000, 6000, step=100)

st.markdown("---")

# Fetch watches
query = supabase.table("watches").select("*")
result = query.execute()
watches = result.data

# Apply filters
if movement_filter != "All":
    watches = [w for w in watches if w["movement_type"] == movement_filter]
watches = [w for w in watches if w["price"] <= max_price]

if not watches:
    st.info("No watches match your current filters.")
    st.stop()

# Display in grid (3 columns)
cols = st.columns(3)
for i, watch in enumerate(watches):
    with cols[i % 3]:
        # Utilizing Streamlit's native container for a clean card border
        with st.container(border=True):
            # BUG FIX 1: Path corrected
            img_path = os.path.join("images", watch["image_filename"])
            
            # BUG FIX 2: use_container_width=True
            st.image(img_path, use_container_width=True)
            
            # Premium HTML Formatting
            st.markdown(f"<div class='watch-brand'>{watch['brand'].upper()}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='watch-model'>{watch['model']}</div>", unsafe_allow_html=True)
            st.markdown(f"*{watch['movement_type']}*", unsafe_allow_html=True)
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
                    st.success(f"Added to cart!")
            else:
                st.error("Out of Stock")