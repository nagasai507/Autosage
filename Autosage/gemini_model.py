
import streamlit as st
import google.generativeai as genai

# Load the API key securely from Streamlit Secrets
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(prompt, image=None):
    if image is not None:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(prompt)

    return response.text
