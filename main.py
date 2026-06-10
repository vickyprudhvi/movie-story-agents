from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

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
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": context}
        ],
    )

    return response.output_text


def save_output(file_name, content):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_DIR / file_name, "w", encoding="utf-8") as f:
        f.write(content)


def extract_director_decision(text):
    try:
        return json.loads(text)
    except Exception:
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                pass

    return {
        "decision": "revise",
        "reason": "Could not parse director decision",
        "revision_focus": ["plot clarity", "stakes", "character motivation"]
    }


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    user_idea_path = Path("user_idea.md")
    user_idea = user_idea_path.read_text(encoding="utf-8")

    print("Step 1: Director creating story development plan...")
    # 1. Director creates story development plan
    director_plan = run_agent(
        "director_agent",
        f"""
        User Idea:
        {user_idea}

        Create a clear story development plan for the specialist agents.

        Return JSON with:
        - genre
        - target_scene_count
        - core_theme
        - must_have_elements
        - story_quality_goals
        - agent_instructions
        """
    )

    print("Step 2: Story Architect building story foundation...")
    # 2. Story Architect follows Director's plan
    story = run_agent(
        "story_architect",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Create the story foundation.
        """
    )

    print("Step 3: Character Agent creating character profiles and arcs...")
    # 3. Character Agent follows Director + Story
    characters = run_agent(
        "character_agent",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Story Foundation:
        {story}

        Create character profiles and arcs.
        """
    )

    print("Step 4: Plot Agent creating scene-level plot outline...")
    # 4. Plot Agent follows Director + Story + Characters
    plot = run_agent(
        "plot_agent",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Story Foundation:
        {story}

        Characters:
        {characters}

        Create the scene-level plot outline.
        """
    )

    print("Step 5: Dialogue Agent writing dialogue for key scenes...")
    # 5. Dialogue Agent follows Director + Story + Characters + Plot
    dialogue = run_agent(
        "dialogue_agent",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Story Foundation:
        {story}

        Characters:
        {characters}

        Plot:
        {plot}

        Create dialogue samples for key scenes.
        """
    )

    print("Step 6: Critic Agent reviewing full story package...")
    # 6. Critic Agent reviews full package
    review = run_agent(
        "critic_agent",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Story Foundation:
        {story}

        Characters:
        {characters}

        Plot:
        {plot}

        Dialogue:
        {dialogue}

        Review the full story package.
        """
    )

    print("Step 7: Director making approve/revise decision...")
    # 7. Director makes approve/revise decision
    director_decision_text = run_agent(
        "director_agent",
        f"""
        User Idea:
        {user_idea}

        Director Plan:
        {director_plan}

        Story Foundation:
        {story}

        Characters:
        {characters}

        Plot:
        {plot}

        Dialogue:
        {dialogue}

        Critic Review:
        {review}

        Decide whether to approve or revise.
        Return only JSON:
        {{
          "decision": "approve" or "revise",
          "reason": "brief explanation",
          "revision_focus": ["focus area 1", "focus area 2"]
        }}
        """
    )

    director_decision = extract_director_decision(director_decision_text)

    revision_history = []

    max_cycles = 2
    cycle = 0

    # 8. Revision loop controlled by Director
    while director_decision.get("decision", "").lower() == "revise" and cycle < max_cycles:
        cycle += 1
        print(f"Revision cycle {cycle}: Director requested revisions — {director_decision.get('reason', '')}")

        revision_history.append(
            f"""
            Revision Cycle {cycle}

            Director Decision:
            {director_decision_text}

            Critic Review:
            {review}
            """
        )

        print(f"  Revision {cycle}.1: Plot Agent revising plot...")
        plot = run_agent(
            "plot_agent",
            f"""
            Revise the plot using Director and Critic feedback.

            User Idea:
            {user_idea}

            Director Plan:
            {director_plan}

            Story Foundation:
            {story}

            Characters:
            {characters}

            Current Plot:
            {plot}

            Critic Review:
            {review}

            Director Decision:
            {director_decision_text}

            Preserve the core story but fix the weaknesses.
            Return the improved plot in the same format.
            """
        )

        print(f"  Revision {cycle}.2: Dialogue Agent rewriting dialogue...")
        dialogue = run_agent(
            "dialogue_agent",
            f"""
            Rewrite dialogue samples based on the revised plot.

            User Idea:
            {user_idea}

            Director Plan:
            {director_plan}

            Story Foundation:
            {story}

            Characters:
            {characters}

            Revised Plot:
            {plot}
            """
        )

        print(f"  Revision {cycle}.3: Critic Agent reviewing revised package...")
        review = run_agent(
            "critic_agent",
            f"""
            Review the revised story package.

            User Idea:
            {user_idea}

            Director Plan:
            {director_plan}

            Story Foundation:
            {story}

            Characters:
            {characters}

            Revised Plot:
            {plot}

            Dialogue:
            {dialogue}
            """
        )

        print(f"  Revision {cycle}.4: Director evaluating revised package...")
        director_decision_text = run_agent(
            "director_agent",
            f"""
            Review the revised package and decide approve or revise.

            User Idea:
            {user_idea}

            Director Plan:
            {director_plan}

            Story Foundation:
            {story}

            Characters:
            {characters}

            Revised Plot:
            {plot}

            Dialogue:
            {dialogue}

            Critic Review:
            {review}

            Return only JSON:
            {{
              "decision": "approve" or "revise",
              "reason": "brief explanation",
              "revision_focus": ["focus area 1", "focus area 2"]
            }}
            """
        )

        director_decision = extract_director_decision(director_decision_text)

    print("Step 9: Saving all outputs...")
    # 9. Save outputs
    save_output("director_plan.txt", director_plan)
    save_output("story.txt", story)
    save_output("characters.txt", characters)
    save_output("plot.txt", plot)
    save_output("dialogue.txt", dialogue)
    save_output("critic_review.txt", review)
    save_output("director_decision.txt", director_decision_text)
    save_output("revision_history.txt", "\n".join(revision_history))

    final_package = f"""
                        # Final Movie Story Package

                        ## Director Plan

                        {director_plan}

                        ---

                        ## Story Foundation

                        {story}

                        ---

                        ## Characters

                        {characters}

                        ---

                        ## Final Plot

                        {plot}

                        ---

                        ## Dialogue

                        {dialogue}

                        ---

                        ## Critic Review

                        {review}

                        ---

## Director Decision

{director_decision_text}

---

## Revision History

{chr(10).join(revision_history)}
"""

    save_output("final_story_package.md", final_package)

    print("Story generation complete.")
    print(f"Director Decision: {director_decision.get('decision')}")
    print("Files saved to outputs/")


if __name__ == "__main__":
    main()