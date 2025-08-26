
from duckduckgo_search import DDGS

def search_scholarships(query):
    results_list = []
    with DDGS() as ddgs:
        for r in ddgs.text(query + " scholarship", max_results=5):
            results_list.append({
                'title': r['title'],
                'link': r['href']
            })
    return results_list
