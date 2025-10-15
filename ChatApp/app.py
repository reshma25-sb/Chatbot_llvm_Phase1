import streamlit as st
import ollama
import time

# Streamlit page setup
st.set_page_config(page_title="Professional Chat App", layout="wide")
st.markdown(
    """
    <h1 style='text-align: center;'>🤖 Self-Hosted LLM Chat – Professional Interface</h1>
    """,
    unsafe_allow_html=True
)

# Session state to store chat messages
if "messages" not in st.session_state:
   st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🤖 Self-Hosted LLM Chat – Professional Interface</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Chat interface
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call local LLM using Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="llama3",  # or "mistral", "grok-3-mini"
                messages=st.session_state.messages
            )
            assistant_reply = response['message']['content']
            st.markdown(assistant_reply)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})