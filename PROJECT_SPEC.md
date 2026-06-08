# Movie Story Agents - Project Specification

## 1. Project Overview

### Project Name

Movie Story Agents

### Version

1.0 (MVP)

### Objective

Build a multi-agent AI storytelling system that transforms a high-level movie idea into a structured story using specialized AI agents.

The system uses a Director Agent to coordinate multiple expert agents responsible for story architecture, character development, plot construction, dialogue generation, and story critique.

The goal is to simulate a collaborative writers' room where multiple agents contribute expertise and improve story quality through iterative feedback.

---

# 2. Business Problem

Traditional LLM story generation relies on a single prompt and often suffers from:

* Weak story structure
* Inconsistent characters
* Plot holes
* Generic dialogue
* Poor long-term story memory

This project addresses these limitations by decomposing storytelling into specialized responsibilities handled by independent AI agents.

---

# 3. Project Goals

### Primary Goals

* Generate movie concepts from user ideas
* Create consistent character arcs
* Build structured three-act stories
* Generate scene-level outlines
* Produce realistic dialogue
* Identify weaknesses through critique agents

### Secondary Goals

* Demonstrate multi-agent architecture
* Explore agent collaboration patterns
* Create a portfolio project showcasing AI engineering skills

---

# 4. System Architecture

```text
User Idea
    │
    ▼
Director Agent
    │
    ├───────────────┐
    │               │
    ▼               ▼
Story Agent   Character Agent
    │               │
    └──────┬────────┘
           ▼
      Plot Agent
           ▼
    Dialogue Agent
           ▼
     Critic Agent
           ▼
    Director Agent
           ▼
      Final Story
```

---

# 5. Agent Definitions

## 5.1 Director Agent

### Purpose

Acts as the central coordinator.

### Responsibilities

* Manage workflow
* Delegate tasks
* Collect outputs
* Resolve conflicts between agents
* Determine revision requirements

### Inputs

* User story idea
* Agent outputs

### Outputs

* Final approved story package

---

## 5.2 Story Architect Agent

### Purpose

Creates the overall narrative structure.

### Responsibilities

* Generate premise
* Define theme
* Define genre
* Create logline
* Build story using Joseph Campbell's 12-stage Hero's Journey

### Outputs

* Story foundation
* 12-stage Hero's Journey breakdown
* Narrative objectives

---

## 5.3 Character Agent

### Purpose

Designs believable characters.

### Responsibilities

* Create protagonist
* Create antagonist
* Define goals
* Define flaws
* Define motivations
* Create character arcs

### Outputs

* Character profiles
* Relationship map
* Character evolution plan

---

## 5.4 Plot Agent

### Purpose

Transforms the story structure into scenes.

### Responsibilities

* Create scene outlines
* Generate conflicts
* Build suspense
* Add twists
* Maintain pacing

### Outputs

* Scene list
* Plot progression
* Story beats

---

## 5.5 Dialogue Agent

### Purpose

Generates realistic conversations.

### Responsibilities

* Write dialogue
* Create unique character voices
* Add emotional depth
* Reduce exposition

### Outputs

* Scene dialogue
* Key conversations
* Emotional exchanges

---

## 5.6 Critic Agent

### Purpose

Reviews story quality.

### Responsibilities

* Identify plot holes
* Detect weak motivations
* Find pacing issues
* Recommend improvements

### Outputs

* Story review
* Improvement suggestions
* Story score

---

# 6. Data Flow

Step 1:
User submits story idea.

Step 2:
Director Agent sends idea to Story Architect Agent.

Step 3:
Story Architect Agent creates story foundation.

Step 4:
Character Agent develops characters.

Step 5:
Plot Agent generates story outline.

Step 6:
Dialogue Agent generates conversations.

Step 7:
Critic Agent reviews generated content.

Step 8:
Director Agent decides whether revisions are required.

Step 9:
Final story package is generated.

---

# 7. Memory Design

## Story Memory

File:
memory/story.json

Stores:

* title
* genre
* theme
* logline
* act summaries

---

## Character Memory

File:
memory/characters.json

Stores:

* names
* goals
* flaws
* arcs
* relationships

---

## Scene Memory

File:
memory/scenes.json

Stores:

* scene id
* location
* participants
* conflict
* outcome

---

# 8. Technology Stack

## Backend

Python 3.12+

## AI Models

* GPT
* Claude
* Gemini

Provider configurable.

## Storage

JSON files

Future:

* SQLite
* PostgreSQL
* Vector Database

## Version Control

Git

Repository hosted on GitHub.

---

# 9. Folder Structure

```text
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
│   └── .gitkeep
│
├── outputs/
│
├── tools/
│
├── main.py
├── requirements.txt
├── README.md
├── PROJECT_SPEC.md
└── .gitignore
```

---

# 10. MVP Scope

Included:

* Director Agent
* Story Agent
* Character Agent
* Plot Agent
* Dialogue Agent
* Critic Agent
* JSON memory
* Command-line execution

Excluded:

* UI
* Database
* Vector search
* Screenplay export
* Multi-user support

---

# 11. Future Enhancements

## Version 2

* World Building Agent
* Continuity Agent
* Screenplay Agent

## Version 3

* LangGraph orchestration
* Agent conversations
* Persistent memory

## Version 4

* Streamlit web application
* Story visualization
* Character relationship graphs

---

# 12. Success Criteria

The system is considered successful when it can:

1. Accept a raw movie idea.
2. Generate a structured story outline.
3. Produce character profiles.
4. Generate scene-level plot progression.
5. Create dialogue samples.
6. Critique its own output.
7. Produce a revised final story package.

---

# 13. Resume Value

This project demonstrates:

* Multi-agent AI architecture
* Prompt engineering
* LLM orchestration
* State management
* Python application design
* Software architecture principles
* Git/GitHub workflow
* AI system design
