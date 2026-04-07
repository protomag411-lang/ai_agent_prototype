
import os
from fastapi import FastAPI, Query
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# 1. CRITICAL SETUP
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

app = FastAPI()

# 2. DEFINE THE AGENTS
manager_agent = Agent(
    role='System Manager',
    goal='Coordinate workflows and manage 95GB data tasks',
    backstory='You are the central brain of a high-performance multi-agent system.',
    llm="google/gemini-1.5-flash",
    verbose=True,
    allow_delegation=False
)

# 3. API ROUTES
@app.get("/")
def health():
    return {"status": "online", "system": "Multi-Agent Coordinator"}

@app.get("/process")
def process_task(query: str = Query(...)):
    """
    Handles GET /process?query=...
    """
    # Define a dynamic task for the agent
    execution_task = Task(
        description=f"Direct Instruction: {query}",
        agent=manager_agent,
        expected_output="A clear summary of the action taken and data retrieved."
    )

    # Initialize the Crew
    system_crew = Crew(
        agents=[manager_agent],
        tasks=[execution_task],
        process=Process.sequential,
        verbose=True
    )

    try:
        result = system_crew.kickoff()
        return {
            "query": query,
            "agent_output": str(result),
            "status": "success"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 4. START COMMAND:
# python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
