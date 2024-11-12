import requests
import json

def fetch_industry_product_data(query, api_key):
    """
    Fetches industry and product understanding data using Serper API.

    Parameters:
    - query: The search query related to industry or product.
    - api_key: Your Serper API key.

    Returns:
    - A dictionary with industry insights or an error message.
    """
    endpoint = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    data = json.dumps({"q": query})

    response = requests.post(endpoint, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data from Serper. Status code: {response.status_code}"}

# Example usage

api_key = '<SERPER-API-KEY>'

api_key = '44f18d81d3b3ba224383661e78d4a854b49d20fb'

query = "AI trends in healthcare"
industry_data = fetch_industry_product_data(query, api_key)

if "error" not in industry_data:
    print("Fetched data from Serper:")
    # Loop through the organic search results and print relevant details
    for result in industry_data.get("organic", []):  # Assuming 'organic' holds the search results
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print(f"Snippet: {result['snippet']}\n")
else:
    print(industry_data["error"])
