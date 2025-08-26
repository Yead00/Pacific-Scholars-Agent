import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

# --- University Scrapers ---
def scrape_uts():
    url = "https://www.uts.edu.au/scholarships"
    headers = {"User-Agent": "Mozilla/5.0"}
    scholarships = []
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        # Scrape scholarship cards
        for item in soup.find_all("div", class_="scholarship-card"):
            title_tag = item.find("h3")
            link_tag = item.find("a")
            if title_tag and link_tag:
                scholarships.append({
                    "title": title_tag.text.strip(),
                    "link": link_tag.get("href")
                })
    except:
        pass
    return scholarships

def scrape_deakin():
    url = "https://www.deakin.edu.au/study/fees-and-scholarships/scholarships"
    headers = {"User-Agent": "Mozilla/5.0"}
    scholarships = []
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        for item in soup.find_all("div", class_="scholarship-item"):
            title_tag = item.find("h3")
            link_tag = item.find("a")
            if title_tag and link_tag:
                scholarships.append({
                    "title": title_tag.text.strip(),
                    "link": link_tag.get("href")
                })
    except:
        pass
    return scholarships

# --- Dynamic web search for additional scholarships ---
def search_online(query="international scholarships australia"):
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=10):
                title = r.get("title", "").strip()
                link = r.get("href", "").strip()
                if title and link and (".edu.au" in link or "scholarship" in link.lower()):
                    results.append({"title": title, "link": link})
    except:
        pass
    return results

# --- Main function to combine everything ---
def get_scholarships(query=None):
    all_scholarships = []
    # Fetch from top universities
    all_scholarships.extend(scrape_uts())
    all_scholarships.extend(scrape_deakin())
    # Add dynamic search if query is provided
    if query:
        all_scholarships.extend(search_online(query))
    # Remove duplicates
    seen = set()
    final = []
    for s in all_scholarships:
        if s['link'] not in seen:
            final.append(s)
            seen.add(s['link'])
    return final
