from agents import tool
from pydantic import BaseModel

class WorkoutPlanInput(BaseModel):
    goal: str
    level: str

@tool
def generate_workout_plan(input: WorkoutPlanInput) -> str:
    return f"""💪 Weekly {input.level} Workout Plan for {input.goal}:
- Mon: Push day
- Tue: Pull day
- Wed: Legs + Core
... (complete plan)
"""
