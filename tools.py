from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import tool
import requests
import os


# get current weather tool

@tool
def get_current_weather(location: str) -> str:
    """useful to get the current weather for a given location"""

    base_url = "http://api.weatherapi.com/v1"
    api_key = os.getenv("WEATHER_API_KEY")
    endpoint = f"/current.json?key={api_key}&q={location}&aqi=no"
    url = base_url + endpoint

    response = requests.get(url)
    weather_data = response.json()
    current_temp = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]
    return f"The current temperature in {location} is {current_temp}°C with {condition}."


# currency conversion tool

@tool
def Usd_to_Inr(amount: float) -> str:
    "Useful to Convert USD to INR"

    base_url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_QMylKjBXtXovDcBt8dfipB8QHhzvnrrGfzhdf3Xk&currencies=INR"

    response = requests.get(base_url)
    data = response.json()
    rate = data["data"]["INR"]["value"]
    inr_amount = amount * rate
    return f"{amount} USD is equal to {inr_amount} INR."


# web search tool

@tool
def web_search(query: str) -> str:
    """
    Useful for when you need to answer questions about current events or look up real-time information.
    """

    google_search = GoogleSerperAPIWrapper()
    result = google_search.run(query)
    return result


# calculator tool

@tool("calculator", description="Perform mathematical calculations.")
def calculator_tool(expression: str) -> str:
    """Useful for when you need to perform Arithematic calculations."""
    return str(eval(expression))
