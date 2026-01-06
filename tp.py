from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemma-3-27b-it",
    contents="Roses are red...",
)

print(response.text)
