from flask import Flask, request, render_template_string, redirect
from datetime import datetime
from workout_generator_v2 import generate_workout_pretty_html

app = Flask(__name__)

# =========================
# HEMSIDAN
# =========================

@app.route("/", methods=["GET", "POST"])
def index():
    workout_html = ""
    if request.method == "POST":
        sport = request.form.get("sport")
        level = request.form.get("level")
        focus = request.form.get("focus")
        duration = request.form.get("duration")
        workout_html = generate_workout_pretty_html(sport, level, focus, duration)

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>RYVAI – Träningsgenerator</title>
<style>
body { font-family: Arial; background:#f4f4f4; padding:40px; }
.container { max-width:800px; background:white; margin:auto; padding:30px;
border-radius:10px; box-shadow:0 0 12px rgba(0,0,0,.1); }
h1 { color:#2c3e50; }
h2 { color:#34495e; }
h3 { color:#16a085; }
select, input, textarea, button { padding:10px; margin-top:8px; width:100%; }
button { background:#2980b9; color:white; border:none; cursor:pointer; border-radius:6px; }
button:hover { background:#3498db; }
hr { margin:40px 0; }
</style>
</head>
<body>
<div class="container">
<h1>RYVAI – AI-baserad träningsgenerator för friidrott</h1>
<form method="post">
<h3>Välj gren</h3>
<select name="sport">
<option value="long_jump">Längdhopp</option>
<option value="triple_jump">Tresteg</option>
<option value="sprint">Sprint</option>
<option value="high_jump">Höjdhopp</option>
<option value="middle_distance">Mellandistans</option>
<option value="shot_put">Kula</option>
<option value="pole_vault">Stavhopp</option>
<option value="javelin">Spjut</option>
</select>
<h3>Nivå</h3>
<select name="level">
<option value="children">Barn</option>
<option value="beginner">Nybörjare</option>
<option value="intermediate">Medel</option>
</select>
<h3>Fokus</h3>
<select name="focus">
<option value="technique">Teknik</option>
<option value="strength">Styrka</option>
<option value="speed">Snabbhet</option>
<option value="mixed">Blandat</option>
</select>
<h3>Passlängd</h3>
<select name="duration">
<option value="30">30 min</option>
<option value="45">45 min</option>
<option value="60">60 min</option>
</select>
<br><br>
<button type="submit">Generera pass</button>
</form>
<hr>
{{ workout_html|safe }}
<hr>
<h2>Hjälp oss förbättra RYVAI</h2>
<form method="post" action="/feedback">
<label>Ditt namn (valfritt)</label>
<input type="text" name="name">
<label>Roll</label>
<select name="role">
<option value="coach">Tränare</option>
<option value="athlete">Aktiv</option>
<option value="parent">Förälder</option>
<option value="other">Annat</option>
</select>
<label>Vad var bra?</label>
<textarea name="good" rows="4" required></textarea>
<label>Vad saknades eller var dåligt?</label>
<textarea name="bad" rows="4" required></textarea>
<label>Skulle du kunna tänka dig att betala för detta i framtiden?</label>
<select name="pay">
<option value="yes">Ja</option>
<option value="maybe">Kanske</option>
<option value="no">Nej</option>
</select>
<label>Vad skulle göra appen värd att betala för?</label>
<textarea name="value" rows="4"></textarea>
<label>Övriga tankar / idéer</label>
<textarea name="extra" rows="4"></textarea>
<br>
<button type="submit">Skicka feedback</button>
</form>
</div>
</body>
</html>
""", workout_html=workout_html)

# =========================
# FEEDBACK ROUTE
# =========================

@app.route("/feedback", methods=["POST"])
def feedback():
    name = request.form.get("name", "Anonym")
    role = request.form.get("role")
    good = request.form.get("good")
    bad = request.form.get("bad")
    pay = request.form.get("pay")
    value = request.form.get("value")
    extra = request.form.get("extra")

    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write("\n------------------------\n")
        f.write(f"Tid: {datetime.now()}\n")
        f.write(f"Namn: {name}\n")
        f.write(f"Roll: {role}\n")
        f.write(f"Bra: {good}\n")
        f.write(f"Dåligt: {bad}\n")
        f.write(f"Betala?: {pay}\n")
        f.write(f"Värde: {value}\n")
        f.write(f"Extra: {extra}\n")

    return redirect("/")

# =========================
# START
# =========================

if __name__ == "__main__":
    app.run(debug=True)
