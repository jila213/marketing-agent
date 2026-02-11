from dotenv import load_dotenv
load_dotenv()

from .marketingagent import root_agent, MarketingIdeationAgent

__all__ = ['root_agent', 'MarketingIdeationAgent']