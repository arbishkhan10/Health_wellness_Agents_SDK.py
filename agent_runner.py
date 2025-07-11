from agents import Agent, OpenAIChatCompletionsModel
from tools.meal_plan import generate_meal_plan
from tools.workout_plan import generate_workout_plan

agent = Agent(
    name="WellnessPlannerAgent",
    instructions="""You are a Health & Wellness Assistant. Collect user's dietary and fitness goals, then generate meal and workout plans using tools. Ask relevant questions. Support streaming.""",
    model=OpenAIChatCompletionsModel(model="gpt-4", stream=True),
    tools=[generate_meal_plan, generate_workout_plan],
    memory=True
)
