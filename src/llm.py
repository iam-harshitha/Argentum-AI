# llm.py
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env")

client = Groq(api_key=groq_api_key)

def query_llama3(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Or use "llama3-70b-8192" if needed
            messages=[
                {"role": "system", "content": "You are a regulated AI financial assistant. Be concise, clear, and compliant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300,  # You can reduce this to make answers shorter
            top_p=1,
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"
