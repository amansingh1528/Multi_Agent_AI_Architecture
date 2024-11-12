
use_cases = [
    "Predictive Maintenance for AI-powered devices",
    "Customer Service Automation with AI Chatbots",
    "AI-based Fraud Detection in Financial Transactions",
    "AI for Personalized Healthcare Recommendations",
    "AI-driven Diagnostics and Imaging Solutions"
]


from agents.genai_usecase import generate_use_case, use_cases

def recommend_resources(use_cases):
    """
    Recommend resources based on AI/GenAI use cases.

    Parameters:
    - use_cases: List of AI/GenAI use cases generated earlier.

    Returns:
    - A dictionary with resource recommendations.
    """
    resources = {}

    for case in use_cases:
        if "Predictive Maintenance" in case:
            resources[case] = ["TensorFlow", "PyTorch", "scikit-learn"]
        elif "AI Chatbots" in case:
            resources[case] = ["Rasa", "Dialogflow", "Microsoft Bot Framework"]

    return resources

# Example usage
resources = recommend_resources(use_cases)
print("Recommended Resources:", resources)
