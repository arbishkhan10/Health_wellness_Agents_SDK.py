from agents import tool
from pydantic import BaseModel

class MealPlanInput(BaseModel):
    goal: str
    preference: str

@tool
def generate_meal_plan(input: MealPlanInput) -> str:
    return f"""🥗 7-Day {input.preference} Meal Plan for {input.goal}:
- Breakfast: Oats with almond milk & banana
- Lunch: Chickpea salad with olive oil dressing
- Dinner: Lentil curry with brown rice
... (repeated for 7 days)
"""
