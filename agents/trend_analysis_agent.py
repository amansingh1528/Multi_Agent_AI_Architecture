import requests
import json

def fetch_market_research_data(query, serper_api_key):
    """
    Fetches market research and trend analysis data using Serper API.

    Parameters:
    - query: The search query for market trends (e.g., "AI trends in healthcare")
    - serper_api_key: Your Serper API key

    Returns:
    - A dictionary with market trend insights or an error message.
    """
    endpoint = "https://google.serper.dev/search"  # Serper API endpoint

    headers = {
        "X-API-KEY": serper_api_key,  # API Key for Serper
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "q": query  # The search query for market research
    })

    response = requests.post(endpoint, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data from Serper. Status code: {response.status_code}"}

# Example usage
serper_api_key = '44f18d81d3b3ba224383661e78d4a854b49d20fb'  # Replace with your Serper API key
query = "AI trends in healthcare"
market_data = fetch_market_research_data(query, serper_api_key)

# Check if data contains an error, otherwise print results
if "error" not in market_data:
    print("Fetched data from Serper:")
    for result in market_data.get("organic", []):  # Assuming 'organic' contains the search results
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print(f"Snippet: {result['snippet']}\n")
else:
    print(market_data["error"])
