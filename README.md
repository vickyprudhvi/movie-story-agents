# Movie Story Agents

A multi-agent AI storytelling system that transforms a high-level movie idea into a structured story using specialized AI agents.

The system simulates a collaborative writers' room where a Director Agent coordinates expert agents — each responsible for a specific layer of the story — and improves quality through iterative critique and revision.

---

## How It Works

```
User Idea
    │
    ▼
Director Agent
    │
    ├─────────────────┐
    ▼                 ▼
Story Architect   Character Agent
    │                 │
    └────────┬────────┘
             ▼
         Plot Agent
             ▼
       Dialogue Agent
             ▼
        Critic Agent
             ▼
       Director Agent
       (revise or approve)
             ▼
        Final Story
```

---

## Agents

| Agent | File | Responsibility |
|-------|------|----------------|
| Director | `agents/director_agent.md` | Coordinates the pipeline, evaluates quality, triggers revisions |
| Story Architect | `agents/story_architect.md` | Builds the story using Joseph Campbell's 12-stage Hero's Journey |
| Character Agent | `agents/character_agent.md` | Designs protagonist, antagonist, and supporting cast |
| Plot Agent | `agents/plot_agent.md` | Creates a 14–18 scene outline mapped to all 12 stages |
| Dialogue Agent | `agents/dialogue_agent.md` | Writes character-specific dialogue for key scenes |
| Critic Agent | `agents/critic_agent.md` | Reviews the full story, scores it 1–10, flags issues |

---

## Story Structure — Joseph Campbell's Hero's Journey

The Story Architect Agent structures every story across all 12 stages:

| Stage | Name | Story Function |
|-------|------|----------------|
| 1 | Ordinary World | Hero's normal life before the adventure |
| 2 | Call to Adventure | A disrupting event presents a challenge |
| 3 | Refusal of the Call | Hero hesitates due to fear or obligation |
| 4 | Meeting the Mentor | A guide provides wisdom or tools |
| 5 | Crossing the Threshold | Hero commits and enters the unknown |
| 6 | Tests, Allies, and Enemies | Challenges faced, alliances formed, foes revealed |
| 7 | Approach to the Inmost Cave | Hero prepares for the central ordeal |
| 8 | The Ordeal | Greatest crisis — death or transformation |
| 9 | The Reward | Hero survives and claims the prize |
| 10 | The Road Back | Return journey, often with new danger |
| 11 | The Resurrection | Final and hardest test — hero is reborn |
| 12 | Return with the Elixir | Hero returns changed and shares the gift |

---

## Memory Files

Agent outputs are stored as JSON in the `memory/` folder:

| File | Contents |
|------|----------|
| `memory/story.json` | Title, genre, theme, logline, all 12 Hero's Journey stages |
| `memory/characters.json` | Protagonist, antagonist, supporting cast, arcs, relationships |
| `memory/scenes.json` | Scene list with conflict, pacing, story beats, dialogue |

---

## Project Structure

```
movie-story-agents/
│
├── agents/
│   ├── director_agent.md
│   ├── story_architect.md
│   ├── character_agent.md
│   ├── plot_agent.md
│   ├── dialogue_agent.md
│   └── critic_agent.md
│
├── memory/
│   ├── story.json
│   ├── characters.json
│   └── scenes.json
│
├── outputs/
│
├── tools/
│
├── user_idea.md
├── main.py
├── requirements.txt
├── PROJECT_SPEC.md
└── README.md
```

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/movie-story-agents.git
cd movie-story-agents
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure environment**

Create a `.env` file in the root directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
CLAUDE_MODEL=claude-haiku-4-5-20251001
```

Get your API key at [console.anthropic.com](https://console.anthropic.com).

**4. Add your movie idea**

Write your movie concept in `user_idea.md`.

**5. Run the system**

```bash
python main.py
```

---

## Output

After a successful run, the system produces:

- `outputs/story.txt` — Story foundation with all 12 Hero's Journey stages
- `outputs/character.txt` — Full character profiles
- `outputs/plot.txt` — Scene-by-scene plot outline
- `outputs/dialogue.txt` — Dialogue for key scenes
- `outputs/review.txt` — Critic's review with score and improvement suggestions

---

## Revision Logic

The Director Agent evaluates the Critic Agent's score and decides:

| Score | Decision |
|-------|----------|
| 8–10 | Approved — final story accepted |
| 6–7 | Accepted with noted weaknesses |
| < 6 | Revision triggered — agents revise and resubmit |

Maximum revision cycles: **2**

---

## Tech Stack

- **Language:** Python 3.12+
- **AI Provider:** Anthropic Claude (configurable)
- **Storage:** JSON files
- **Version Control:** Git

---

## Project Progress

### Completed

| Item | Status | Notes |
|------|--------|-------|
| `PROJECT_SPEC.md` | Done | Full specification with Hero's Journey structure |
| `agents/director_agent.md` | Done | Role, workflow, revision logic defined |
| `agents/story_architect.md` | Done | 12-stage Hero's Journey output schema |
| `agents/character_agent.md` | Done | Protagonist, antagonist, arc, relationship map |
| `agents/plot_agent.md` | Done | Scene distribution across all 12 stages |
| `agents/dialogue_agent.md` | Done | Key scene dialogue with subtext |
| `agents/critic_agent.md` | Done | Scoring rubric and revision trigger logic |
| `user_idea.md` | Done | Story concept — *Legacy Protocol* spy thriller |
| `main.py` | Partial | Basic pipeline working (loads agents, calls OpenAI, saves outputs) |
| `outputs/` | Done | story.txt, character.txt, plot.txt, dialogue.txt, review.txt generated |
| `.gitignore` | Done | `.env`, `outputs/`, `user_idea.md` excluded |
| `README.md` | Done | This file |

---

### Pending

| Item | Priority | What Needs to Be Done |
|------|----------|-----------------------|
| `main.py` — Director Agent logic | High | Add revision cycle: read critic score, loop agents if score < 7, max 2 iterations |
| `main.py` — Memory saving | High | Save agent outputs to `memory/story.json`, `memory/characters.json`, `memory/scenes.json` |
| `requirements.txt` | High | List dependencies (`openai`, `python-dotenv`, etc.) |
| `.env.example` | Medium | Template file showing required environment variables |
| `tools/` — Memory manager | Medium | Utility to read/write JSON memory files cleanly |
| Dialogue coverage | Medium | Dialogue Agent currently generates 3 scenes — should cover all key scenes (5 priority scenes per spec) |
| Error handling in `main.py` | Medium | Handle API failures, missing files, JSON parse errors |
| `main.py` — Provider config | Low | Make AI provider switchable (OpenAI / Claude / Gemini) via `.env` |

---

### Current `main.py` Capabilities

```
✅ Loads agent system prompts from agents/*.md
✅ Calls OpenAI GPT-4.1-mini for each agent
✅ Runs pipeline: Story → Character → Plot → Dialogue → Critic
✅ Saves all outputs to outputs/ folder
❌ Director Agent not implemented (no revision cycles)
❌ Memory files (story.json, characters.json, scenes.json) not saved
❌ No error handling
```

---

## Example Story Concept

See `user_idea.md` for the current story being developed — *Legacy Protocol*, a spy espionage thriller about a retired covert operative named Veer who is pulled back into the field when his former Commanding Officer's death triggers a secret Legacy Protocol tied to off-the-books intelligence assets.

---

## Future Enhancements

**Version 2**
- World Building Agent
- Continuity Agent
- Screenplay Agent

**Version 3**
- LangGraph orchestration
- Persistent vector memory

**Version 4**
- Streamlit web application
- Character relationship graphs
- Story visualization
