from flask import Flask, render_template, request
from scraper import get_scholarships

import os  # For Render PORT environment variable

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    results = get_scholarships(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=False)


