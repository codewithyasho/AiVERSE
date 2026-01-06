from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def run_gemma(query: str) -> str:
    response = client.models.generate_content(
        model="gemma-3-27b-it",
        contents=query
    )
    return response.text

# result = run_gemma("Explain the theory of relativity in simple terms.")
# print(result)
