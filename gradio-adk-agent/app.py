import gradio as gr
from google.adk.models import Gemini
from agent.marketing_agent import MarketingAgent

model = Gemini(model_name="gemini-1.5-pro")
agent = MarketingAgent(model)

def generate(product, target_group, goal, task):
    return agent.run(product, target_group, goal, task)

with gr.Blocks() as demo:
    gr.Markdown("# 📢 Marketing Agent")

    product = gr.Textbox(label="Produkt")
    target_group = gr.Textbox(label="Zielgruppe")
    goal = gr.Textbox(label="Marketingziel")

    task = gr.Dropdown(
        ["Werbetext", "Produktbeschreibung", "Kampagnenidee"],
        label="Aufgabe"
    )

    output = gr.Textbox(label="Ergebnis", lines=10)
    btn = gr.Button("Generieren")

    btn.click(generate, [product, target_group, goal, task], output)

demo.launch()
