import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def explain_meme(meme_text):

    prompt = f"""
You are a meme understanding assistant.

Meme Text:
{meme_text}

Return EXACTLY:

MEANING:
(one short sentence)

EMOTION:
(one word)

NARRATION:
(2-3 short sentences)

Keep everything concise.
"""

    response = model.generate_content(
        prompt
    )

    return response.text