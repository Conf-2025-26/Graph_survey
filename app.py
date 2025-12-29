from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = request.form.get("choice")

        with open("votes.csv", "a", newline="") as f:
            csv.writer(f).writerow([choice])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
