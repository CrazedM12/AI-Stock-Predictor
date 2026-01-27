import google.generativeai as genai

genai.configure(api_key="AIzaSyB9fRtPFRsNMuUbXlLMkB_AHxmTf2c-5fU")
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini_old_english(message):
    prompt = f"""
Thou shalt respond in noble old English,
with the tone of a medieval sage or chronicler.
Let thy words be archaic, poetic, and wise.

The user asketh: "{message}"
"""
    response = model.generate_content(prompt)
    print(response.text)

ask_gemini_old_english("Explain the economy")
