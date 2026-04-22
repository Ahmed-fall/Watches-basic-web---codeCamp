import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🤖 AI Watch Expert")

if not st.session_state.get("logged_in"):
    st.warning("Please sign in to chat with the AI.")
    st.stop()

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