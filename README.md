Travel Planner Agent is a small CLI application that accepts trip preferences, runs a CrewAI-based planner, and prints a personalized itinerary. The README describes three agents and destination research, day-by-day planning, and budget breakdowns. The CLI-to-crew call is visible in the excerpt; the agent implementation was not sampled, so links from the crew to those documented capabilities are unverified.
# Travel Planner Agent

Three-agent CrewAI system that creates personalized travel itineraries with destination research, day-by-day plans, and budget breakdown.

**Framework**: CrewAI  
**LLM**: GPT-4o-mini  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python agent.py --destination "Tokyo, Japan" --days 7 --budget 3000
python agent.py --destination "Paris, France" --days 5 --budget 5000 --interests "art, wine, architecture"
```
<img width="6216" height="4189" alt="diagram" src="https://github.com/user-attachments/assets/0e6cb788-fe58-4900-ba76-6c49c8489e6b" />
