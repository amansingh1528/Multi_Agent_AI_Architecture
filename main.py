from agents.agent import fetch_serper_data
from agents.trend_analysis_agent import fetch_market_research_data
from agents.Industry import fetch_industry_product_data
from agents.genai_usecase import generate_use_case
from agents.resource_reccomendation_agent import recommend_resources
from agents.collaboration_agent import collaborate_with_crew_agents
from agents.validation import validate_and_refine

def multi_agent_system(query, serper_api_key, feedback):
    # Data Ingestion Agent
    data = fetch_serper_data(query, serper_api_key)

    # Market Research and Trend Analysis Agent
    market_data = fetch_market_research_data(data, serper_api_key)

    # Industry and Product Understanding Agent
    industry_data = fetch_industry_product_data(market_data, serper_api_key)

    # AI/GenAI Use Case Generation Agent
    use_cases = generate_use_case(industry_data)

    # Resource Recommendation Agent
    resource_recommendations = recommend_resources(use_cases)

    # CrewAI Collaboration Agent
    collaboration_result = collaborate_with_crew_agents(use_cases, resource_recommendations, industry_data)

    # Validation and Feedback Loop
    validation_result = validate_and_refine(collaboration_result, feedback)

    return validation_result

# Example usage
query = "AI applications in healthcare"
feedback = "The results need more emphasis on healthcare-specific use cases."
final_result = multi_agent_system(query, '44f18d81d3b3ba224383661e78d4a854b49d20fb', feedback)
print(final_result)

