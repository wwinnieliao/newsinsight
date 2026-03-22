import feedparser
import requests

def fetch_techcrunch():
    """Fetch recent articles from TechCrunch RSS feed."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get('https://techcrunch.com/feed/', headers=headers, timeout=10)
    feed = feedparser.parse(response.content)
    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.get('summary', ''),
            'source': 'TechCrunch'
        })
    return articles

def fetch_zdnet():
    """Fetch recent articles from ZDNet RSS feed."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get('https://www.zdnet.com/news/rss.xml', headers=headers, timeout=10)
    feed = feedparser.parse(response.content)
    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.get('summary', ''),
            'source': 'ZDNet'
        })
    return articles

def fetch_gartner():
    """Fetch recent articles about Gartner using Google News RSS to bypass blocks."""
    url = 'https://news.google.com/rss/search?q=site:gartner.com+AI+OR+robotics+OR+manufacturing&hl=en-US&gl=US&ceid=US:en'
    headers = {'User-Agent': 'Mozilla/5.0'}
    articles = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        feed = feedparser.parse(response.content)
        for entry in feed.entries:
            articles.append({
                'title': entry.title.split(' - ')[0],  # Google news appends publisher name
                'link': entry.link,
                'summary': '', # Google News often has cluttered snippets, skip them
                'source': 'Gartner'
            })
    except Exception as e:
        print(f"Error fetching Gartner: {e}")
        
    return articles

def fetch_all():
    articles = []
    try:
        articles.extend(fetch_techcrunch())
    except Exception as e:
        print(f"Error in TechCrunch: {e}")
        
    try:
        articles.extend(fetch_zdnet())
    except Exception as e:
        print(f"Error in ZDNet: {e}")
        
    try:
        articles.extend(fetch_gartner())
    except Exception as e:
        print(f"Error in Gartner: {e}")
    
    return articles

if __name__ == "__main__":
    # Test execution
    articles = fetch_all()
    print(f"Fetched {len(articles)} total articles.")
    for a in articles[:10]:
        print(f"- [{a['source']}] {a['title']}")
