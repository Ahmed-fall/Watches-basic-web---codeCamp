import os
import base64
import streamlit as st
import google.generativeai as genai


# 1. Page Config
st.set_page_config(page_title="AI Watch Expert | WatchVault", page_icon="", layout="wide")

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
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

set_background(os.path.join("images", "9.jpg"))

# 3. Premium Scoped CSS
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
    </style>
""", unsafe_allow_html=True)

# 4. Header UI
st.markdown("""
<div class="page-title-container">
    <div class="page-title"> Horology AI Expert</div>
    <div class="page-subtitle">Consult our master watchmaker to find your perfect timepiece.</div>
</div>
""", unsafe_allow_html=True)

# 5. Authentication Check (Using your original logic with premium styling)
if not st.session_state.get("logged_in"):
    st.markdown("""
    <div class="auth-warning">
        Please sign in to chat with the AI.
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# 6. EXACT Original AI Logic (Untouched)
SYSTEM_PROMPT = """You are an elite horologist and watch consultant for WatchVault, a premium watch store.
Your role is to help customers choose the perfect watch from our collection of 8 models:

1. Watch Acti (ActionX) — Quartz, $299 — Rugged sport watch, 100m water resistant
2. SOS 911 (TacForce) — Quartz, $449 — Tactical watch, emergency signaling bezel
3. Call Emergency (ResQ) — Automatic, $599 — Professional dive-style, sapphire crystal
4. Mercy (Mercy) — Quartz, $899 — Slim elegant dress watch
5. Hub 9 (HubNine) — Automatic, $1,299 — Swiss-inspired, visible caseback, date
6. Aureon (Aureon) — Automatic, $2,499 — Luxury limited production
7. Virelli (Virelli) — Mechanical, $3,499 — Italian hand-wound, 72h power reserve
8. Luminor (Luminor) — Automatic, $4,999 — Icon cushion-case dive watch, 300m

Ask about the user's lifestyle, budget, style preferences, and occasion to give personalized advice.
Be concise, knowledgeable, and passionate about horology. Respond in 2-4 short paragraphs max."""

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview", system_instruction=SYSTEM_PROMPT)

# Display history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):  
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask me anything about watches...")

if user_input:
    # Show user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build history for Gemini
    gemini_history = []
    for msg in st.session_state.chat_history[:-1]:  # exclude last user message
        gemini_history.append({
            "role": msg["role"],
            "parts": [msg["content"]]
        })

    chat = model.start_chat(history=gemini_history)
    response = chat.send_message(user_input)
    reply = response.text

    st.session_state.chat_history.append({"role": "model", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)