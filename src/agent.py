import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

@CrewBase
class TravelPlannerCrew:
    """Travel Planner Agent Crew setup using external configurations."""

    # Absolute paths relative to this file location help prevent directory execution bugs
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    agents_config = os.path.join(base_dir, 'config', 'agents.yaml')
    tasks_config = os.path.join(base_dir, 'config', 'tasks.yaml')

    def __init__(self) -> None:
        # Common LLM configuration used across all defined agents
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

    @agent
    def destination_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['destination_researcher'],
            llm=self.llm,
            verbose=True  
        )

    @agent
    def travel_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_planner'],
            llm=self.llm,
            verbose=True  
        )

    @agent
    def budget_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_analyst'],
            llm=self.llm,
            verbose=True  
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task']
        )

    @task
    def budget_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_task']
        )

    @crew
    def crew(self) -> Crew:
        """Assembles the agents and tasks into a sequential execution workflow."""
        return Crew(
            agents=self.agents,  # Automatically gathered by @agent decorators
            tasks=self.tasks,    # Automatically gathered by @task decorators
            process=Process.sequential,
            verbose=True  
        )
