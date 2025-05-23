# ai_engine.py

from dotenv import load_dotenv
import os
from google.generativeai import configure, GenerativeModel

# Load env and configure Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
configure(api_key=api_key)

# Load Gemini Model once
model = GenerativeModel("gemini-1.5-flash")

def generate_responses(prompt_text):
    try:
        casual_prompt = f"Explain like I'm 10 years old: {prompt_text}"
        formal_prompt = f"Explain formally and academically: {prompt_text}"

        casual_response = model.generate_content(casual_prompt).text
        formal_response = model.generate_content(formal_prompt).text

        return casual_response, formal_response

    except Exception as e:
        print(f"❌ Error generating response: {e}")
        return "Error generating casual response.", "Error generating formal response."
