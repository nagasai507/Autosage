from google import generativeai as genai

# 🔴 Paste your API key here
genai.configure(api_key="AIzaSyCis98-b9qavzMoKXE4OIm4T03ui2zt9aA")

# ✅ Latest supported model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(prompt, image=None):

    if image:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(prompt)

    return response.text