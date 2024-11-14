import requests
import json


# Define a function to fetch data from Serper

def fetch_serper_data(query, api_key):
    """
    Fetches relevant search results from Serper API based on a given query.

    Parameters:

    - query: The search query string (e.g., "AI applications in healthcare")

    - api_key: Your Serper API key

    Returns:
    - A dictionary containing search results from Serper API or an error message.
    """

    endpoint = "https://google.serper.dev/search"  # Correct endpoint from your cURL example

    # Set headers with the API key and content type
    headers = {
        "X-API-KEY": api_key,  # Use the correct API key header
        "Content-Type": "application/json",  # Set content type to JSON
    }


    # Prepare the payload data (query in JSON format)
    data = json.dumps({
        "q": query  # The search query parameter
    })

    # Make the POST request to the Serper API
    response = requests.post(endpoint, headers=headers, data=data)

    # Ensure that the query is a string
    if not isinstance(query, str):
        raise ValueError("Query must be a string.")

    # Prepare the payload data (query in JSON format)
    data = {
        "q": query,  # The search query parameter as a string
        "type": "search",  # Define the type if needed
        "engine": "google"  # Specify the engine used for the search
    }

    # Make the POST request to the Serper API
    response = requests.post(endpoint, headers=headers, json=data)  # Use json= instead of data=


    if response.status_code == 200:
        # Return the JSON data if the request is successful
        return response.json()
    else:
        # Handle errors and return the error message
        return {"error": f"Failed to fetch data from Serper. Status code: {response.status_code}"}

# Example usage

api_key = '<SERPER-API-KEY>'  # Replace with your actual API key # Replace with your actual API key

query = "AI applications in healthcare"  # Example search query
data = fetch_serper_data(query, api_key)

# Check if data contains an error, otherwise print results
if "error" not in data:
    print("Fetched data from Serper:")
    # Loop through the organic search results and print relevant details
    for result in data.get("organic", []):  # Assuming 'organic' holds the search results
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print(f"Snippet: {result['snippet']}\n")
else:
    print(data["error"])
