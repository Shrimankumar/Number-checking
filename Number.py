from flask import Flask, render_template_string, request
import threading

app = Flask(__name__)

html_page = """
<form method="POST">
    <input type="number" name="number" required>
    <button type="submit">Check</button>
</form>
<h3>{{ result }}</h3>
"""

@app.route("/", methods=["GET", "POST"])
def check_number():
    result = ""
    if request.method == "POST":
        num = int(request.form["number"])
        if num < 0:
            result = "Negative Number"
        elif num > 0:
            result = "Positive Number"
        else:
            result = "Zero"
    return render_template_string(html_page, result=result)

def run_app():
  app.run(debug=False, use_reloader=False)

threading.Thread(target=run_app).start()
