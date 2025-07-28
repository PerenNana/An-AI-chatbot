import streamlit as st
import requests

API_URL = "http://localhost:8000/assist"

st.set_page_config(page_title="Chatbot", layout="centered")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 Chatbot")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Enter your message...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple chatbot logic (replace with real model)
    response = requests.post(
        API_URL,
        json={"message": prompt},
        headers={"Content-Type": "application/json"}
    )

    responded = response.json().get("response", "No response received.")

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": responded})
    with st.chat_message("assistant"):
        st.markdown(responded)

# Clear chat button
clear_button = st.button("🧹 Clear Chat")
if clear_button and st.session_state.messages == []:
    st.error("No chat history to clear.")
elif clear_button:
    st.session_state.messages = []
    st.experimental_rerun()
    st.success("Chat history cleared.")