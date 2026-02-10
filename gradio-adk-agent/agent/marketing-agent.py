from google.adk.agents import Agent
from agent.prompts import (
    copywriting_prompt,
    product_description_prompt,
    campaign_idea_prompt
)

class MarketingAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="MarketingAgent",
            model=model,
            description="AI agent for marketing content generation"
        )

    def run(self, product, target_group, goal, task):
        if task == "Werbetext":
            return copywriting_prompt(product, target_group, goal)
        elif task == "Produktbeschreibung":
            return product_description_prompt(product, target_group)
        elif task == "Kampagnenidee":
            return campaign_idea_prompt(product, target_group, goal)
        else:
            return "Unbekannte Aufgabe."
