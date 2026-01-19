from google_client import google_agent
from agents import agents

query = input("Enter your query: ")

## Agents INITIALIZATION ##

# Deepseek Agent
try:
    deepseek_agent = agents(
        model="ollama:deepseek-v3.1:671b-cloud", query=query)
except Exception as e:
    deepseek_agent = f"Can't Proceed Your Request...SORRY!!: {e}"

# OpenAI Agent
try:
    openai_agent = agents(model="ollama:gpt-oss:120b-cloud", query=query)
except Exception as e:
    openai_agent = f"Can't Proceed Your Request...SORRY!!: {e}"

# Qwen Agent
try:
    qwen_agent = agents(model="groq:qwen/qwen3-32b", query=query)
except Exception as e:
    qwen_agent = f"Can't Proceed Your Request...SORRY!!: {e}"

# llama Agent
try:
    llama_agent = agents(model="groq:llama-3.3-70b-versatile", query=query)
except Exception as e:
    llama_agent = f"Can't Proceed Your Request...SORRY!!: {e}"

# kimi Agent
try:
    kimi_agent = agents(
        model="groq:moonshotai/kimi-k2-instruct-0905", query=query)
except Exception as e:
    kimi_agent = f"Can't Proceed Your Request...SORRY!!: {e}"

# google Agent
try:
    google_agent = google_agent(prompt=query)
except Exception as e:
    google_agent = f"Can't Proceed Your Request...SORRY!!: {e}"


## Agents EXECUTION ##

print("\nDeepseek Agent Response:\n", deepseek_agent)
print("\nOpenAI Agent Response:\n", openai_agent)
print("\nQwen Agent Response:\n", qwen_agent)
print("\nLlama Agent Response:\n", llama_agent)
print("\nKimi Agent Response:\n", kimi_agent)
print("\nGoogle Agent Response:\n", google_agent)
