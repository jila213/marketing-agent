"""
Agent definitions for the Business Intelligence pipeline.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from dotenv import load_dotenv
from .tools import get_database_schema, execute_sql_and_format

load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"

# Text-to-SQL Agent
text_to_sql_agent = LlmAgent(
    model=GEMINI_MODEL,
    name='text_to_sql_agent',
    description="Converts natural language questions to SQL queries.",
    instruction="""
Du bist ein SQL-Experte. Konvertiere die Benutzeranfrage in eine SQL-Abfrage.

REGELN:
1. Nutze IMMER zuerst get_database_schema um die Datenbankstruktur zu sehen
2. Nur SELECT-Abfragen sind erlaubt
3. Gib NUR die SQL-Abfrage zurück, keine Erklärungen
4. Keine Markdown-Codeblöcke
""",
    tools=[get_database_schema]
)

# SQL Executor Agent
sql_executor_agent = LlmAgent(
    model=GEMINI_MODEL,
    name='sql_executor_agent',
    description="Executes SQL queries and returns results.",
    instruction="""
Du führst SQL-Abfragen aus. Nutze das execute_sql_and_format Tool mit der SQL-Abfrage.
Gib die Ergebnisse formatiert zurück.
""",
    tools=[execute_sql_and_format]
)

# Explanation Agent
explanation_agent = LlmAgent(
    model=GEMINI_MODEL,
    name='explanation_agent',
    description="Explains query results in plain language.",
    instruction="""
Erkläre die Datenbank-Ergebnisse in einfacher, verständlicher Sprache.
Fasse die wichtigsten Erkenntnisse zusammen.
"""
)

# Root Agent (Sequential Pipeline)
root_agent = SequentialAgent(
    name='bi_agent',
    description="Business Intelligence Agent für Datenbankabfragen",
    sub_agents=[
        text_to_sql_agent,
        sql_executor_agent,
        explanation_agent
    ]
)