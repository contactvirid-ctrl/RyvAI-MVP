import json
import random
from pathlib import Path
import generic_templates_v2 as generic_templates  # vår templates-fil

exercise_dir = Path("./")  # mappen med exercises

# ----------------------------
# Hjälpfunktioner
# ----------------------------
def load_json(file):
    """Ladda JSON-fil från exercises-mappen"""
    with open(exercise_dir / file, encoding="utf-8") as f:
        return json.load(f)

def get_value(ex):
    """Hämta repetitions / duration / prescription"""
    return ex.get("prescription") or ex.get("reps") or ex.get("duration") or ""

def pick(exercises, category, amount):
    """Plocka 'amount' exercises från 'category', slumpmässigt"""
    pool = [e for e in exercises if e["category"] == category]
    if len(pool) < amount:
        return pool
    return random.sample(pool, amount)

# ----------------------------
# Generator med snygg terminal-output
# ----------------------------
def generate_workout_pretty(sport, level, focus, duration):
    """
    sport: str, t.ex. "triple_jump"
    level: "children", "beginner", "intermediate"
    focus: "Technique", "Strength", "Speed", "Mixed"
    duration: int, t.ex. 30, 45, 60
    """

    # Ladda exercises
    sport_file = f"exercises_{sport}_v1.json"
    try:
        exercises = load_json(sport_file)
    except FileNotFoundError:
        print(f"Fel: Filen {sport_file} finns inte!")
        return "Inga övningar hittades."

    warmup_fallback = load_json("exercises_general_warmup_v1.json")
    strength_fallback = load_json("exercises_general_strength_v1.json")
    play = load_json("exercises_play_v1.json") if level=="children" else []

    # Hämta template
    templates = generic_templates.templates
    if focus not in templates[level]:
        focus = "Mixed"
    template = templates[level][focus][0]

    output = []
    output.append(f"\n=== PASS: {sport.replace('_',' ').title()} – {level.capitalize()} – {focus} – {duration} min ===\n")

    for section in template["sections"]:
        block_name = section["name"]
        count = section["exerciseCount"]
        cats = section["allowedCategories"]

        if count == 0:
            continue

        output.append(f"--- {block_name} ({count} övningar) ---")

        collected = []

        for cat in cats:
            picked = pick(exercises, cat, count)
            collected.extend(picked)
            count -= len(picked)

        # Fallback om inte tillräckligt
        if count > 0:
            if "strength" in [c.lower() for c in cats]:
                fallback = random.sample(strength_fallback, count)
            else:
                fallback = random.sample(warmup_fallback, count)
            collected.extend(fallback)

        # Play-block för children
        if block_name.lower() == "play / coordination" and level=="children":
            collected = random.sample(play, section["exerciseCount"])

        # Skriv ut övningar snyggt
        for i, ex in enumerate(collected, start=1):
            val = get_value(ex)
            line = f"{i}. {ex['name']}"
            if val:
                line += f" ({val})"
            if "description" in ex:
                line += f" → {ex['description']}"
            output.append(line)

        output.append("")  # tom rad mellan block

    output.append("=== PASS KLART! ===\n")
    return "\n".join(output)

# ----------------------------
# Test i terminal med svenska frågor
# ----------------------------
if __name__ == "__main__":

    print("=== UNIVERSAL WORKOUT GENERATOR ===\n")

    # Sporter
    sports = {
        "1": ("Tre steg / Long Jump", "long_jump"),
        "2": ("Tresteg / Triple Jump", "triple_jump"),
        "3": ("Sprint", "sprint"),
        "4": ("Höjdhopp", "high_jump"),
        "5": ("Mellandistans", "middle_distance"),
        "6": ("Kula", "shot_put"),
        "7": ("Stavhopp", "pole_vault"),
        "8": ("Spjut", "javelin")
    }

    print("Välj gren:")
    for k, v in sports.items():
        print(f"{k}: {v[0]}")
    sport_choice = input("Skriv siffran för din gren: ").strip()
    sport_name = sports[sport_choice][1]

    # Nivå
    print("\nVälj nivå:")
    print("1: Barn")
    print("2: Nybörjare")
    print("3: Medel")
    level_map = {"1":"children","2":"beginner","3":"intermediate"}
    level_choice = input("Skriv siffran för nivå: ").strip()
    level = level_map[level_choice]

    # Fokus
    print("\nVad vill du fokusera på?")
    print("1: Teknik")
    print("2: Styrka")
    print("3: Snabbhet")
    print("4: Blandat")
    focus_map = {"1":"Technique","2":"Strength","3":"Speed","4":"Mixed"}
    focus_choice = input("Skriv siffran för fokus: ").strip()
    focus = focus_map[focus_choice]

    # Passlängd
    duration = int(input("\nHur lång ska passet vara (30/45/60): ").strip())

    output = generate_workout_pretty(sport_name, level, focus, duration)
    print(output)
