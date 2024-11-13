# Multi-Agent AI System for Industry-Specific AI & GenAI Use Case Generation

This project is a multi-agent architecture designed to generate relevant AI and Generative AI (GenAI) use cases for a given company or industry. The system performs market research, analyzes industry and product insights, and recommends resources for implementing AI/ML solutions. It is built to enhance both operational efficiency and customer experience.

## Table of Contents
- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Agents](#agents)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)

## Project Overview
The Multi-Agent AI System is designed to:
1. Conduct market research and analyze trends for a specified industry or company.
2. Understand industry-specific needs and potential for AI applications.
3. Generate relevant AI/GenAI use cases.
4. Provide actionable resources and recommendations.
5. Enable collaboration between various agents.
6. Incorporate a validation and feedback loop for continuous improvement.

## System Architecture
The system uses multiple agents working together:
1. **Data Ingestion Agent** - Fetches data from external sources like Serper API.
2. **Market Research and Trend Analysis Agent** - Analyzes trends using IBM WatsonX.
3. **Industry and Product Understanding Agent** - Gathers insights on industry-specific challenges and opportunities.
4. **AI/GenAI Use Case Generation Agent** - Generates AI use cases based on the research data.
5. **Resource Recommendation Agent** - Suggests tools, frameworks, and documentation for implementation.
6. **CrewAI Collaboration Agent** - Collaborates across agents for refined insights.
7. **Validation and Feedback Agent** - Validates output and incorporates feedback.

## Agents
### Data Ingestion Agent (`agent.py`)
Fetches relevant search data from Serper API to gather industry and product information.

### Market Research and Trend Analysis Agent (`trend_analysis_agent.py`)
Uses WatsonX to analyze current trends in the specified industry based on ingested data.

### Industry and Product Understanding Agent (`industry_understanding_agent.py`)
Parses and processes data to understand industry-specific pain points and opportunities for AI.

### AI/GenAI Use Case Generation Agent (`genai_usecase.py`)
Generates AI and GenAI use cases based on insights from industry and market analysis.

### Resource Recommendation Agent (`resource_reccomendation_agent.py`)
Suggests resources, frameworks, and tools to help implement the AI use cases.

### CrewAI Collaboration Agent (`collaboration_agent.py`)
Facilitates collaboration across agents to refine use case suggestions and resource recommendations.

### Validation and Feedback Loop (`validation.py`)
Provides validation and feedback to continuously improve the system outputs.

## Getting Started
### Prerequisites
- Python 3.10+
- Required libraries: `requests`, `json`

### Set up API keys:
- Serper API for data ingestion.

### Requirments
- requests==2.31.0
- python-dotenv==1.0.0
- crewai

## Usage
- Update main.py with the query string and API keys.
- Run the system: 
      python main.py
- Output will display:
      Relevant AI/GenAI use cases
      Resource recommendations
      Collaboration insights
      Validation results
## File Structure
```plaintext
MultiAgentAI
│
├── agents/                     # Directory containing all agents
│   ├── agent.py         # Serper data ingestion
│   ├── trend_analysis_agent.py         # WatsonX trend analysis
│   ├── industry.py # Industry and product insights
│   ├── genai_usecase.py    # AI/GenAI use case generation
│   ├── resource_reccomendation_agent.py # Resource recommendation
│   ├── collaboration.py          # CrewAI collaboration
│   └── validation.py             # Validation and feedback
│
├── main.py                     # Main file to run the multi-agent system
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
