import feedparser

url = "https://techcrunch.com/feed/"

feed = feedparser.parse(url)

entry = feed.entries[0]

print(entry.summary)
