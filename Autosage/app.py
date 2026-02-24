import streamlit as st
from gemini_model import get_gemini_response
from PIL import Image

st.title("🚗 AutoSage AI Assistant")

option = st.radio("Choose Input Type",
                  ("Text Problem", "Image Problem"))

# TEXT INPUT
if option == "Text Problem":

    text = st.text_area("Describe vehicle issue")

    if st.button("Analyze"):
        prompt = f"""
        You are an automobile expert.
        Explain problem, cause and solution.

        Problem: {text}
        """

        result = get_gemini_response(prompt)
        st.write(result)

# IMAGE INPUT
else:

    file = st.file_uploader("Upload dashboard image")

    if file:
        image = Image.open(file)
        st.image(image)

        if st.button("Analyze Image"):
            prompt = "Explain dashboard warning symbols."
            result = get_gemini_response(prompt, image)
            st.write(result)