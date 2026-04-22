import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
import os
import json

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

st.markdown("""
    <style>
    .cart-total { font-size: 2rem; font-weight: 700; color: #D9381E; }
    </style>
""", unsafe_allow_html=True)

st.title("🛒 Your Cart")

if not st.session_state.get("logged_in"):
    st.warning("Please sign in to view your cart.")
    st.stop()

cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty. Go explore some watches!")
    st.stop()

st.markdown(f"**{len(cart)} item(s) in your cart**")
st.markdown("---")

total = 0
for i, item in enumerate(cart):
    with st.container(border=True):
        c1, c2, c3 = st.columns([1, 3, 1], vertical_alignment="center")
        with c1:
            # BUG FIX: Path corrected
            img_path = os.path.join("images", item["image"])
            st.image(img_path, width=80)
        with c2:
            st.markdown(f"**{item['brand']} — {item['model']}**")
            st.markdown(f"${item['price']:,.2f}")
        with c3:
            if st.button("Remove", key=f"remove_{i}", use_container_width=True):
                st.session_state.cart.pop(i)
                st.rerun()
        total += item["price"]

st.markdown("---")
st.markdown(f"<div align='right'>Subtotal: <span class='cart-total'>${total:,.2f}</span></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

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