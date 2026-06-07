from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

local_api_key = os.getenv("OPENAI_API_KEY")

AGENTS_DIR = Path("agents")
OUTPUT_DIR = Path("outputs")



client = OpenAI(api_key=local_api_key)

def load_agent(agent_name):
    path = AGENTS_DIR / f"{agent_name}.md"
    return path.read_text(encoding="utf-8")

def run_agent(agent_name, context):
    prompt = load_agent(agent_name)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{"role": "system", "content": prompt}, 
                {"role": "user", "content": context}],
    )

    return response.output_text

def main():
    user_idea_path = Path("user_idea.md")
    user_idea = user_idea_path.read_text(encoding="utf-8")
    
    # user_idea = """
    # A retired spy named Veer discovers his former handler is dead,
    # and a hidden legacy protocol pulls him into a global conspiracy.
    # """

    story = run_agent("story_architect", user_idea)
    characters = run_agent("character_agent", story)
    plot = run_agent("plot_agent", story + characters)
    dialogue = run_agent("dialogue_agent", story + characters + plot)
    review = run_agent("critic_agent", story + characters + plot + dialogue)

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