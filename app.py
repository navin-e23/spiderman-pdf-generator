"""
🕷️ Spider-Man PDF Generator — app.py
Flask web app that generates personalized Spider-Man themed PDFs on the fly.
"""

from flask import Flask, render_template, request, send_file, jsonify
from pdf_generator import generate_hero_card
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    """Receive form data and return a generated Spider-Man PDF."""
    data = {
        "name":       request.form.get("name", "Peter Parker"),
        "alias":      request.form.get("alias", "Your Friendly Neighbourhood Hero"),
        "city":       request.form.get("city", "New York"),
        "power":      request.form.get("power", "Spider-Sense"),
        "quote":      request.form.get("quote", "With great power comes great responsibility."),
        "strength":   request.form.get("strength", "85"),
        "agility":    request.form.get("agility", "95"),
        "intelligence": request.form.get("intelligence", "90"),
    }

    pdf_path = generate_hero_card(data)

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=f"spiderman_card_{data['name'].replace(' ', '_')}.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
