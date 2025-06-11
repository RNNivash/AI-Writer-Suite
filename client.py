import requests
import streamlit as st

st.title("AI Writer Suite: Gemini Essays & LLaMA Poems")

st.caption("© Nivash R N | 2025")
input_text = st.text_input("Enter a topic:")

col1, col2 = st.columns(2)

def get_gemini_response(topic):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"topic": topic}
        )
        if response.status_code == 200:
            return response.json().get("content", "No content found.")
        return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Connection error: {str(e)}"

def get_ollama_response(topic):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"topic": topic}
        )
        if response.status_code == 200:
            return response.json().get("content", "No content found.")
        return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Connection error: {str(e)}"

with col1:
    if st.button("Generate Essay with Gemini"):
        if input_text:
            with st.spinner("Generating essay..."):
                output = get_gemini_response(input_text)
                st.success("Essay Generated:")
                st.write(output)
        else:
            st.warning("Please enter a topic.")

with col2:
    if st.button("Generate Poem with LLaMA"):
        if input_text:
            with st.spinner("Generating poem..."):
                output = get_ollama_response(input_text)
                st.success("Poem Generated:")
                st.write(output)
        else:
            st.warning("Please enter a topic.")