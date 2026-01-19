from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

def google_agent(prompt: str) -> str:
    
    response = client.models.generate_content(
        model="gemma-3-27b-it",
        contents=f"""
        You are a helpful assistant. Be concise and answer the user query in short:

        {prompt}
        """,
    )

    result = response.text

    return result

