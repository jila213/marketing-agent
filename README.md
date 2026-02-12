# Marketing Agent (Google ADK + Gradio)

Ein produktionsnaher **Marketing-Ideation-Agent** auf Basis von **Google ADK (Agent Development Kit)** mit **zwei Interfaces**:

- **ADK Dev UI** (zum Debuggen/Trace der Agenten-Ausführung)
- **Gradio App** (benutzerfreundliche Oberfläche für Marketing-Inputs)

Der Agent generiert kreative Marketinginhalte (z. B. **Kampagnenideen, Werbetexte, Produktbeschreibungen**) auf Grundlage von **Produkt/Service**, **Zielgruppe**, **Marketingziel** und einer **Aufgabenwahl**. Zusätzlich können Ergebnisse **iterativ verfeinert** und über ein **Sterne-Feedback** bewertet werden.

---

## 🎯 Projektziele

- Einen KI-Agenten entwickeln, der Marketing-Outputs strukturiert und zielgruppenspezifisch erstellt
- Google ADK in einer sauberen Projektstruktur anwenden (Agent + Runner + Prompt-Datei)
- Eine intuitive UI bereitstellen (Gradio) inkl.:
  - Eingabemaske
  - Ergebnisanzeige
  - Verfeinerungsfunktion (Human-in-the-loop)
  - Nutzerfeedback (Sterne + Kommentar)
- Den Agent zusätzlich im **ADK Dev UI** verfügbar machen (für Nachvollziehbarkeit & Debugging)

---

## ✨ Funktionen

### Gradio App
- Eingaben:
  - **Produkt / Service**
  - **Zielgruppe**
  - **Marketingziel**
  - **Aufgabe** (Dropdown: Kampagnenidee / Werbetext / Produktbeschreibung)
- Ausgabe:
  - Generiertes Ergebnis (Markdown-formatiert)
- **Ergebnis verfeinern**:
  - Nutzer gibt Anpassungsanweisung ein (z. B. „kürzer“, „mehr Humor“, „Social Media Fokus“)
  - Agent liefert vollständig überarbeitete Version
- **Kundenfeedback**:
  - Sternebewertung (1–5) + optionaler Kommentar
- Grundlegende Validierung & Fehlerbehandlung (z. B. Pflichtfelder, leere Antworten, Exceptions)

### ADK Dev UI
- Auswahl des Agents (`marketing_agent` / ggf. weiterer Agent wie `bi_agent`)
- Trace/State/Events für transparente Agenten-Ausführung

---

## 🧠 Agent-Architektur (Google ADK)

Das Projekt enthält **zwei Agenten**, die im ADK Dev UI auswählbar sind:

1. **`marketing_agent`** (unser Marketing-Ideation-Agent)  
2. **`bi_agent`** (zusätzlicher Agent aus der Vorlage / Beispiel-Agent)

Im Fokus dieser App steht **`marketing_agent`**, der über einen **LlmAgent** mit klarer Systeminstruktion (`SYSTEM_PROMPT`) gesteuert wird.

### Marketing-Agent (Kernlogik)

- **Prompt Engineering**: Der Agent nutzt einen strukturierten System-Prompt (inkl. Context, Objective, Style, Constraints, Few-Shot Example).
- **Output-Format**: Finaler Output wird in **Markdown** ausgegeben (fette Überschriften, Bullet-Points).
- **Verlässlichkeit**: Der Prompt enthält klare Constraints (keine erfundenen Produktfakten, keine generischen Floskeln) und einen internen Denkprozess.

### Ablauf (Gradio → ADK)

1. User gibt Produkt/Service, Zielgruppe, Marketingziel und Aufgabe ein  
2. App erstellt daraus einen Prompt  
3. ADK `LlmAgent` generiert das Ergebnis  
4. Optional: User verfeinert das Ergebnis über eine Anpassungsanweisung  
5. Optional: User gibt Sterne-Feedback + Kommentar

---

## 🛠️ Tech Stack

- **Python** (empfohlen: 3.12+)
- **uv** (Dependency Management)
- **Google ADK** (LlmAgent, InMemoryRunner)
- **Gemini** (z. B. `gemini-2.5-flash`)
- **Gradio** (UI)

---

## ✅ Voraussetzungen

- Python 3.12+  
- `uv` installiert  
- **Gemini API Key** (Google AI Studio)

---

## 🚀 Installation & Start

### 1) Repository klonen
```bash
git clone <EURE_REPO_URL>
cd marketing-agent
```


### 2) Dependencies installieren
```bash
uv sync
```
Öffnen: http://127.0.0.1:8000/dev-ui/

### 3) Environment konfigurieren

Lege eine .env Datei an (oder kopiere .example.env, falls vorhanden) und trage ein:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4) Gradio App starten
```bash
uv run app.py
```

### 5) ADK Dev UI starten (optional)
```bash
uv run adk web
```

--- 

## 🧑‍💻 Nutzung (Gradio)

1. Produkt / Service eintragen (z. B. „Nachhaltige Trinkflasche“)

2. Zielgruppe definieren (z. B. „Studierende, umweltbewusst“)

3. Marketingziel angeben (z. B. „Markenbekanntheit steigern“)

4. Aufgabe wählen (Kampagnenidee / Werbetext / Produktbeschreibung)

5. „Generieren“ klicken

6. Optional: Unter „Ergebnis verfeinern“ eine Anpassungsanweisung eingeben und „Verfeinern“ klicken

7. Optional: Sternebewertung + Kommentar absenden

---

## 📌 Prompt-Konzept (SYSTEM_PROMPT)

Der Marketing-Agent wird über einen System-Prompt gesteuert, der u. a. folgende Punkte enthält:

- Marketing-Frameworks (z. B. AIDA, PAS)
- Sauberes Markdown-Format im Output
- Klare Struktur für Kampagnenideen:
  - Kampagnenname  
  - Headline  
  - Zentrale Botschaft  
  - Kreativer Hook  
  - Empfohlene Kanäle  
  - Call-to-Action  
- Constraints:
  - keine erfundenen Produktfakten  
  - keine generischen Floskeln  
  - Tone-of-Voice beachten  
- Few-Shot Example zur Stabilisierung der Qualität
---

## 📂 Projektstruktur (Beispiel)
```
.
├── agents/
│   ├── bi_agent/                     # zusätzlicher Agent (Vorlage / Beispiel)
│   └── marketing_agent/              # unser Marketing-Agent
│       ├── __init__.py
│       ├── marketingagent.py         # LlmAgent + InMemoryRunner + run()
│       └── prompts.py                # SYSTEM_PROMPT
├── app.py                            # Gradio UI
├── pyproject.toml                    # Dependencies (uv)
├── README.md
└── .env                              # API Key (nicht committen)
```
---
## 🧩 Herausforderungen & Lernerfahrungen (Reflexion)

### Herausforderungen

Prompt Engineering: Zu Beginn erhielten wir teilweise unspezifische oder inkonsistente Ergebnisse, da unser Prompt noch nicht ausreichend strukturiert war. Durch die Ergänzung von COMPASS und Chain of thought kamen dann bessere Ergebnisse.

Verfeinerungsausgabe: Verfeinerung musste so integriert werden, dass sie nicht „nochmal neu“ generiert, sondern wirklich das bestehende Ergebnis überarbeitet.

Verbindung mit der Datenbank, da wir Probleme hatten die Extension richtig zu verbinden.

Technische Herausforderungen waren Fehlermeldungen aufgrund der Pfade und Ordnerstruktur.

Des Weiteren gab es manchmal Probleme, bezüglich des API Schlüssels, dass dieser erschöpft wäre.

### Lernerfahrungen

Aufbau einer ADK-basierten Agenten-App in einer wartbaren Struktur (Prompts, Agent-Logik, UI getrennt)

Wie stark die Output-Qualität von klaren Format- und Constraint-Regeln abhängt

Praktische Umsetzung iterativer Content-Erstellung (Generate → Refine → Feedback)