from pathlib import Path

AGENTS_DIR = Path("agents")
OUTPUT_DIR = Path("outputs")

def load_agent(agent_name):
    path = AGENTS_DIR / f"{agent_name}.md"
    return path.read_text(encoding="utf-8")

def run_agent(agent_name, context):
    prompt = load_agent(agent_name)
    print(f"\n--- Running {agent_name} ---\n")
    print("SYSTEM PROMPT:")
    print(prompt[:300])
    print("\nCONTEXT:")
    print(context[:500])

    return f"Output from {agent_name}"

def main():
    user_idea = """
    A retired spy named Veer discovers his former handler is dead,
    and a hidden legacy protocol pulls him into a global conspiracy.
    """

    story = run_agent("story_architect", user_idea)
    characters = run_agent("character_agent", story)
    plot = run_agent("plot_agent", story + characters)
    dialogue = run_agent("dialogue_agent", plot)
    review = run_agent("critic_agent", dialogue)

    print("\nFinal Review:")
    print(review)
    with open(  OUTPUT_DIR / "story.txt", "w", encoding="utf-8") as f:
        f.write(story)
    with open(  OUTPUT_DIR / "character.txt", "w", encoding="utf-8") as f:
        f.write(characters)
    with open(  OUTPUT_DIR / "plot.txt", "w", encoding="utf-8") as f:
        f.write(plot)
    with open(  OUTPUT_DIR / "dialogue.txt", "w", encoding="utf-8") as f:
        f.write(dialogue)
    with open(  OUTPUT_DIR / "review.txt", "w", encoding="utf-8") as f:
        f.write(review)

if __name__ == "__main__":
    main()