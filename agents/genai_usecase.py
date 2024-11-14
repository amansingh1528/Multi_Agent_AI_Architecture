
from agents.Industry import fetch_industry_product_data, industry_data

def generate_use_case(data):
    """
    Generate AI/GenAI use cases based on industry data.

    Parameters:
    - data: Industry data or product data retrieved from market research.

    Returns:
    - A list of potential AI/GenAI use cases.
    """
    # Example: Use case generation logic based on industry data.
    use_cases = []

    if "AI" in data.get("query", "").lower():
        use_cases.append("Predictive Maintenance for AI-powered devices")
        use_cases.append("Customer Service Automation with AI Chatbots")

    return use_cases

# Example usage
use_cases = generate_use_case(industry_data)
# Print the generated use cases
print("Generated Use Cases:")
for case in use_cases:
    print(f"- {case}")
