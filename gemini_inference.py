˜import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
gemkey = os.getenv('GEMINI_KEY')

genai.configure(api_key = gemkey)
model = genai.GenerativeModel(
    "gemini-pro"
)

def respond(user_query):
    prompt_design = f"Respond to this query {user_query} in a general SHORT manner"
    response = model.generate_content(prompt_design)
    
    return response.text