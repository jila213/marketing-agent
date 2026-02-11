import gradio as gr
from agents.marketing_agent.marketingagent import MarketingIdeationAgent
# Agent initialisieren
agent = MarketingIdeationAgent(model="gemini-2.5-flash")


def generate_campaign(product, target_group, goal, task):
    """
    Ruft den Marketing-Agenten auf und gibt das Ergebnis zurück.
    """
    if not product or not target_group or not goal:
        return "⚠️ Bitte fülle alle Felder aus.", gr.update(interactive=False)

    try:
        result = agent.run(
            product=product,
            target_group=target_group,
            goal=goal,
            task=task
        )
        if not result or result.strip() == "":
            return "⚠️ Keine Antwort vom Agent erhalten. Bitte versuche es erneut.", gr.update(interactive=False)
        return result, gr.update(interactive=True)
    except Exception as e:
        return f"❌ Fehler bei der Generierung: {str(e)}", gr.update(interactive=False)


def refine_result(current_result, refinement_instruction, product, target_group, goal, task):
    """
    Verfeinert das aktuelle Ergebnis basierend auf Benutzer-Feedback.
    """
    if not current_result or current_result.startswith("⚠️") or current_result.startswith("❌"):
        return "⚠️ Bitte generiere zuerst ein Ergebnis, bevor du es verfeinerst."
    
    if not refinement_instruction or refinement_instruction.strip() == "":
        return "⚠️ Bitte gib eine Anpassungsanweisung ein."

    try:
        refinement_prompt = f"""
Produkt: {product}
Zielgruppe: {target_group}
Marketingziel: {goal}
Aufgabe: {task}

Hier ist das bisherige Ergebnis:
---
{current_result}
---

Bitte passe das Ergebnis basierend auf folgendem Feedback an:
{refinement_instruction}

Gib das vollständig überarbeitete Ergebnis aus.
"""
        result = agent._run_async(refinement_prompt)
        if not result or result.strip() == "":
            return "⚠️ Keine Antwort vom Agent erhalten. Bitte versuche es erneut."
        return result
    except Exception as e:
        return f"❌ Fehler bei der Verfeinerung: {str(e)}"


def clear_all():
    """Setzt alle Felder zurück."""
    return "", "", "", "Kampagnenidee", "", "", gr.update(interactive=False)


with gr.Blocks() as demo:
    gr.Markdown("# 📢 Marketing Ideation Agent")
    gr.Markdown(
        "Dieser Agent generiert kreative Marketinginhalte "
        "auf Basis von Produkt, Zielgruppe und Marketingziel."
    )

    with gr.Row():
        product = gr.Textbox(
            label="Produkt / Service",
            placeholder="z. B. Nachhaltige Trinkflasche"
        )
        target_group = gr.Textbox(
            label="Zielgruppe",
            placeholder="z. B. Studierende, umweltbewusst"
        )

    goal = gr.Textbox(
        label="Marketingziel",
        placeholder="z. B. Markenbekanntheit steigern"
    )

    task = gr.Dropdown(
        choices=[
            "Kampagnenidee",
            "Werbetext",
            "Produktbeschreibung"
        ],
        value="Kampagnenidee",
        label="Aufgabe"
    )

    output = gr.Textbox(
        label="Generiertes Ergebnis",
        lines=14
    )

    with gr.Row():
        btn = gr.Button("🚀 Generieren", variant="primary")
        clear_btn = gr.Button("🗑️ Zurücksetzen")

    # Verfeinerungsbereich
    gr.Markdown("---")
    gr.Markdown("### 🔧 Ergebnis verfeinern")
    gr.Markdown("Gib Anpassungswünsche ein, um das generierte Ergebnis zu verbessern.")
    
    refinement_input = gr.Textbox(
        label="Anpassungsanweisung",
        placeholder="z. B. 'Mache es kürzer', 'Füge mehr Humor hinzu', 'Fokussiere auf Social Media'",
        lines=2
    )
    
    refine_btn = gr.Button("✨ Verfeinern", interactive=False)

    # Status-Anzeige
    status = gr.Markdown("")

    # Event-Handler
    btn.click(
        generate_campaign,
        inputs=[product, target_group, goal, task],
        outputs=[output, refine_btn]
    )
    
    refine_btn.click(
        refine_result,
        inputs=[output, refinement_input, product, target_group, goal, task],
        outputs=output
    )
    
    clear_btn.click(
        clear_all,
        outputs=[product, target_group, goal, task, output, refinement_input, refine_btn]
    )

demo.launch()