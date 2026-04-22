import os
import json
import base64
import streamlit as st
from supabase import create_client, Client

# 1. Page Config
st.set_page_config(page_title="Cart | WatchVault", page_icon="🛒", layout="wide")

# 2. Database Connection Fix
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# 3. Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "cart" not in st.session_state:
    st.session_state.cart = []
if "user_id" not in st.session_state:
    st.session_state.user_id = None

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

# 5. Premium Scoped CSS
st.markdown("""
    <style>
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
        color: #D4AF37; /* Rich Gold */
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
    .cart-total { 
        font-size: 2rem; 
        font-weight: 700; 
        color: #D4AF37; /* Upgraded from Red to Gold to match theme */
    }
    .cart-item-brand {
        color: #D4AF37;
        font-size: 1.1rem;
        font-weight: bold;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# 6. Header UI
st.markdown("""
<div class="page-title-container">
    <div class="page-title">🛒 Secure Cart</div>
    <div class="page-subtitle">Review your selected timepieces before finalizing your acquisition.</div>
</div>
""", unsafe_allow_html=True)

# 7. Authentication & Empty Cart Checks
if not st.session_state.get("logged_in"):
    st.markdown("""
    <div class="auth-warning">
        Please access the <b>Auth</b> menu to sign in before viewing your cart.
    </div>
    """, unsafe_allow_html=True)
    st.stop()

cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty. Go explore the collection to add some watches!")
    st.stop()

# 8. Cart Items Render
st.markdown(f"**{len(cart)} item(s) in your cart**")
st.markdown("---")

total = 0
for i, item in enumerate(cart):
    with st.container(border=True):
        c1, c2, c3 = st.columns([1, 3, 1], vertical_alignment="center")
        with c1:
            img_path = os.path.join("images", item["image"])
            if os.path.exists(img_path):
                st.image(img_path, width=80)
            else:
                st.warning("Image missing")
        with c2:
            st.markdown(f"<div class='cart-item-brand'>{item['brand'].upper()}</div>", unsafe_allow_html=True)
            st.markdown(f"**{item['model']}**")
            st.markdown(f"${item['price']:,.2f}")
        with c3:
            if st.button("Remove", key=f"remove_{i}", use_container_width=True):
                st.session_state.cart.pop(i)
                st.rerun()
        total += item["price"]

st.markdown("---")
st.markdown(f"<div align='right'>Subtotal: <span class='cart-total'>${total:,.2f}</span></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 9. Checkout Logic
# Right-align the checkout button
_, checkout_col = st.columns([3, 1])
with checkout_col:
    if st.button("✅ Secure Checkout", type="primary", use_container_width=True):
        try:
            supabase.table("orders").insert({
                "user_id":     st.session_state.user_id,
                "total_price": total,
                "items":       json.dumps(cart)
            }).execute()
            st.session_state.cart = []
            st.success("Order placed successfully! Thank you for shopping at WatchVault.")
            st.balloons()
        except Exception as e:
            st.error(f"Checkout failed: {e}")