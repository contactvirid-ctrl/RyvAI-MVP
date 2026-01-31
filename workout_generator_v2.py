import json
import random
from pathlib import Path
import generic_templates_v2 as generic_templates

exercise_dir = Path("./")

# ----------------------------
# Hjälpfunktioner
# ----------------------------
def load_json(file):
    with open(exercise_dir / file, encoding="utf-8") as f:
        return json.load(f)

def get_value(ex):
    return ex.get("prescription") or ex.get("reps") or ex.get("duration") or ""

def pick(exercises, category, amount):
    pool = [e for e in exercises if e["category"] == category]
    if len(pool) < amount:
        return pool
    return random.sample(pool, amount)

# ----------------------------
# Returnerar pass som dict
# ----------------------------
def generate_workout(sport, level, focus, duration):
    sport_file = f"exercises_{sport}_v1.json"
    try:
        exercises = load_json(sport_file)
    except FileNotFoundError:
        print(f"Fel: Filen {sport_file} finns inte!")
        return {}

    warmup_fallback = load_json("exercises_general_warmup_v1.json")
    strength_fallback = load_json("exercises_general_strength_v1.json")
    play = load_json("exercises_play_v1.json") if level=="children" else []

    # Templates och fallback
    templates = generic_templates.templates
    level_templates = templates[level]
    focus_key = focus.lower()
    if focus_key in level_templates:
        template_list = level_templates[focus_key]
    else:
        # fallback: ta första key om fokus saknas
        first_key = next(iter(level_templates))
        template_list = level_templates[first_key]

    template = template_list[0]  # detta används för resten

    plan = {}
    for section in template["sections"]:
        block_name = section["name"]
        count = section["exerciseCount"]
        cats = section["allowedCategories"]

        if count == 0:
            continue

        collected = []
        for cat in cats:
            picked = pick(exercises, cat, count)
            collected.extend(picked)
            count -= len(picked)

        if count > 0:
            if "strength" in [c.lower() for c in cats]:
                fallback = random.sample(strength_fallback, count)
            else:
                fallback = random.sample(warmup_fallback, count)
            collected.extend(fallback)

        if block_name.lower() == "play / coordination" and level=="children":
            collected = random.sample(play, section["exerciseCount"])

        plan[block_name] = []
        for i, ex in enumerate(collected, start=1):
            val = get_value(ex)
            line = f"{i}. {ex['name']}"
            if val:
                line += f" ({val})"
            if "description" in ex:
                line += f" → {ex['description']}"
            plan[block_name].append(line)

    return plan

# ----------------------------
# Returnerar HTML-version för Flask
# ----------------------------
def generate_workout_pretty_html(sport, level, focus, duration):
    plan = generate_workout(sport, level, focus, duration)
    if not plan:
        return "<p>Inga övningar hittades.</p>"

    html = f"<pre style='font-family: monospace; font-size: 16px;'>"
    html += f"=== PASS: {sport.replace('_',' ').title()} – {level.capitalize()} – {focus} – {duration} min ===\n\n"
    for section, exercises in plan.items():
        html += f"--- {section} ({len(exercises)} övningar) ---\n"
        for ex in exercises:
            html += f"{ex}\n"
        html += "\n"
    html += "=== PASS KLART! ===</pre>"
    return html

# ----------------------------
# Terminaltest med frågor
# ----------------------------
if __name__ == "__main__":
    print("=== UNIVERSAL WORKOUT GENERATOR ===\n")

    # Sporter
    sports = {
        "1": ("Längdhopp", "long_jump"),
        "2": ("Tresteg", "triple_jump"),
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
    sport = sports[sport_choice][1]

    # Nivå
    print("\nVälj nivå:")
    print("1: Barn\n2: Nybörjare\n3: Medel")
    level_map = {"1":"children","2":"beginner","3":"intermediate"}
    level_choice = input("Skriv siffran för nivå: ").strip()
    level = level_map[level_choice]

    # Fokus
    print("\nVad vill du fokusera på?")
    print("1: Teknik\n2: Styrka\n3: Snabbhet\n4: Blandat")
    focus_map = {"1":"Technique","2":"Strength","3":"Speed","4":"Mixed"}
    focus_choice = input("Skriv siffran för fokus: ").strip()
    focus = focus_map[focus_choice]

    # Passlängd
    duration = int(input("\nHur lång ska passet vara (30/45/60): ").strip())

    print("\n" + generate_workout_pretty_html(sport, level, focus, duration))
