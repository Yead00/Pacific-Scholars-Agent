from flask import Flask, render_template, request
from scraper import search_scholarships

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_scholarships(query)
    return render_template("index.html", results=results, query=query)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)



