from concurrent.futures import ThreadPoolExecutor, as_completed
from google_client import google_agent
from agents import agents

query = input("Enter your query: ")

# -------------------------
# Wrap each agent in a function
# -------------------------


def run_agent(name, fn):
    try:
        return name, fn()
    except Exception as e:
        return name, f"Can't process the request...CHECK FOR NEXT RESPONSE --> \n Details: {e}"


# -------------------------
# Define tasks
# -------------------------
tasks = [
    ("DeepSeek", lambda: agents(model="ollama:deepseek-v3.1:671b-cloud", query=query)),
    ("OpenAI", lambda: agents(model="ollama:gpt-oss:120b-cloud", query=query)),
    ("Qwen", lambda: agents(model="groq:qwen/qwen3-32b", query=query)),
    ("Llama", lambda: agents(model="groq:llama-3.3-70b-versatile", query=query)),
    ("Kimi", lambda: agents(model="groq:moonshotai/kimi-k2-instruct-0905", query=query)),
    ("Google", lambda: google_agent(prompt=query)),
]

# -------------------------
# Run all in parallel
# -------------------------
with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
    futures = [executor.submit(run_agent, name, fn) for name, fn in tasks]

    for future in as_completed(futures):
        name, result = future.result()
        print(f"\n{name} Agent Response:\n{result}")
