import streamlit as st
from agent_runner import agent
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="🧘‍♀️ Faj's Health & Wellness AI", layout="centered")

if "chat" not in st.session_state:
    st.session_state.chat = []

st.title("🌱 Faj's AI Health & Wellness Planner")
st.markdown("_Get your personal wellness plan powered by AI!_")

col1, col2, col3 = st.columns(3)
if col1.button("Lose 5kg"):
    st.session_state.chat.append(("user", "I want to lose 5kg in 2 months"))
if col2.button("I'm vegetarian"):
    st.session_state.chat.append(("user", "I'm vegetarian"))
if col3.button("I'm diabetic"):
    st.session_state.chat.append(("user", "I'm diabetic"))

msg = st.text_input("💬 Ask your wellness assistant anything")
if st.button("Send") and msg.strip():
    st.session_state.chat.append(("user", msg))

for role, text in st.session_state.chat:
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(text)

for i, (role, text) in enumerate(st.session_state.chat):
    if role == "user" and (i == len(st.session_state.chat) - 1):
        with st.spinner("Thinking..."):
            for chunk in agent.stream(text):
                st.session_state.chat.append(("agent", chunk))
                st.rerun()
