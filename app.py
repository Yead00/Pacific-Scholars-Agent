from flask import Flask, request, render_template_string
from scraper import get_scholarships

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "").strip()
    scholarships = get_scholarships(query)

    html = """
    <h2>Pacific Scholars AI Agent</h2>
    <form method="post">
        <input type="text" name="query" placeholder="Search scholarships, jobs, research..." value="{{query}}" style="width:400px;">
        <button type="submit">Search</button>
    </form>
    <ul>
    """
    if scholarships:
        for s in scholarships:
            html += f"<li><a href='{s['link']}' target='_blank'>{s['title']}</a></li>"
    else:
        html += "<li>No scholarships found. Try a different keyword.</li>"
    html += "</ul>"

    return render_template_string(html, query=query)

if __name__ == "__main__":
    app.run(debug=True)


