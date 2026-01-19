from tools import get_current_weather, Usd_to_Inr, web_search, calculator_tool
from langchain.agents import create_agent


# =================== Agent Configuration ===================

def agents(model: str, query: str) -> str:
    '''
    Main function to create and run the agent with the provided model and user query.
    '''

    agent = create_agent(
        model=model,
        system_prompt="You are a helpful assistant. Be concise and short. Answer the user's queries using the available tools when necessary.",
        tools=[get_current_weather, Usd_to_Inr, web_search, calculator_tool],
    )

    response = agent.invoke({
        "messages": [{
            "role": "user",
            "content": query
        }]
    })

    result = response["messages"][-1].content

    return result
