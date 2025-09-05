import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def google_search(query):
    url = f"https://www.google.com/search?q={query}"

    # Use fake user agent to mimic a real browser
    headers = { 
        "User-Agent" : UserAgent().random 
    }

    # Send HTTP GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch search results. Status code {response.status_code}")
        
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Search Results:")
    # Extract search result titles and links
    results = []
    for g in soup.find_all("div", class_="MjjYud"):
        title = g.find("h3").text if g.find("h3") else "No title"
        link = g.find("a")["href"] if g.find("a") else "No link"
        results.append({"title": title, "link": link})

    return results

print(google_search('python programming'))