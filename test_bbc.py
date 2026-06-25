import requests

url = "https://feeds.bbci.co.uk/news/world/middle_east/rss.xml"

try:
    response = requests.get(url, timeout=20)

    print("Status Code:", response.status_code)
    print("Length:", len(response.text))

    print("\nFirst 500 chars:\n")
    print(response.text[:500])

except Exception as e:
    print("ERROR:", e)