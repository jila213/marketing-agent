from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import InMemoryRunner
from google.genai import types
import asyncio
from dotenv import load_dotenv
from .prompts import SYSTEM_PROMPT

load_dotenv()


class MarketingIdeationAgent:
    def __init__(self, model: str = "gemini-2.5-flash"):
        self.agent = LlmAgent(
            name="marketing_ideation_agent",
            model=model,
            instruction=SYSTEM_PROMPT
        )
        self.runner = InMemoryRunner(
            agent=self.agent,
            app_name="marketing_agent"
        )

    def run(self, product, target_group, goal, task):
        prompt = f"""
Produkt: {product}
Zielgruppe: {target_group}
Marketingziel: {goal}
Aufgabe: {task}

Erstelle eine passende Marketingausgabe für die angegebene Aufgabe.
"""
        return self._run_async(prompt)
    
    def _run_async(self, prompt: str) -> str:
        async def _execute():
            session = await self.runner.session_service.create_session(
                app_name="marketing_agent",
                user_id="user"
            )
            
            content = types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)]
            )
            
            result_text = ""
            async for event in self.runner.run_async(
                user_id="user",
                session_id=session.id,
                new_message=content
            ):
                if hasattr(event, 'content') and event.content:
                    parts = getattr(event.content, 'parts', None)
                    if parts:
                        for part in parts:
                            text = getattr(part, 'text', None)
                            if text:
                                result_text += text
            
            return result_text if result_text else "Keine Antwort vom Agent erhalten."
        
        return asyncio.run(_execute())


# Für ADK Web Interface
root_agent = LlmAgent(
    name="marketing_ideation_agent",
    model="gemini-2.5-flash",
    instruction=SYSTEM_PROMPT
)