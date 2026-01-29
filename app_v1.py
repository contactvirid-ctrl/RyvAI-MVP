from flask import Flask, render_template_string, request
from workout_generator_v2 import generate_workout_pretty

app = Flask(__name__)

# ----------------------------
# Flask-route
# ----------------------------
@app.route("/", methods=["GET","POST"])
def index():
    workout_output = ""
    if request.method == "POST":
        # Hämta värden från formuläret
        sport = request.form.get("sport")
        level = request.form.get("level")
        focus = request.form.get("focus")
        duration = int(request.form.get("duration"))

        # Generera pass
        workout_output = generate_workout_pretty(sport, level, focus, duration).replace("\n","<br>")

    # HTML-formulär och resultat
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>RYVAI – Workout Generator</title>
<style>
body { font-family: Arial; background:#f4f4f4; padding:30px; }
.container { max-width:800px; background:white; margin:auto; padding:25px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,.1);}
h1 { color:#2c3e50; }
select, button { padding:8px; margin-top:10px; width:100%; max-width:300px; }
button { background:#2980b9; color:white; border:none; cursor:pointer; }
button:hover { background:#3498db; }
hr { margin:20px 0; }
</style>
</head>
<body>
<div class="container">
<h1>RYVAI – Workout Generator</h1>
<form method="post">

<label>Välj gren:</label><br>
<select name="sport">
<option value="long_jump">Tre steg / Long Jump</option>
<option value="triple_jump">Tresteg / Triple Jump</option>
<option value="sprint">Sprint</option>
<option value="high_jump">Höjdhopp</option>
<option value="middle_distance">Mellandistans</option>
<option value="shot_put">Kula</option>
<option value="pole_vault">Stavhopp</option>
<option value="javelin">Spjut</option>
</select>

<br>
<label>Välj nivå:</label><br>
<select name="level">
<option value="children">Barn</option>
<option value="beginner">Nybörjare</option>
<option value="intermediate">Medel</option>
</select>

<br>
<label>Vad vill du fokusera på?</label><br>
<select name="focus">
<option value="Technique">Teknik</option>
<option value="Strength">Styrka</option>
<option value="Speed">Snabbhet</option>
<option value="Mixed">Blandat</option>
</select>

<br>
<label>Passlängd:</label><br>
<select name="duration">
<option value="30">30 min</option>
<option value="45">45 min</option>
<option value="60">60 min</option>
</select>

<br><br>
<button type="submit">Generera pass</button>
</form>

<hr>
<div>
{{ workout_output|safe }}
</div>
</div>
</body>
</html>
""", workout_output=workout_output)

# ----------------------------
# Starta server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
