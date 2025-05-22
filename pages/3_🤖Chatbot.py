import streamlit as st
import requests

# 🔐 Replace this with your real Groq API key
API_KEY = "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"

API_URL = "https://api.groq.com/openai/v1/chat/completions"

# 📍 Headers for Groq
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 🧠 Ask LLaMA-4 on Groq
def ask_llama(prompt):
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that answers questions about India's culture and tourism."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# --- Streamlit App ---
st.title("🧠 Cultural Travel Chatbot ")

user_input = st.text_input("Ask your cultural tourism question here:")

if user_input:
    with st.spinner("Thinking..."):
        answer = ask_llama(user_input)
        st.markdown(f"**🤖 Response:** {answer}")
