import feedparser
import time

from config import RSS_FEEDS


def fetch_all_news():

    all_news = []

    for source_name, rss_url in RSS_FEEDS.items():

        print(f"[RSS] {source_name}")

        try:

            feed = feedparser.parse(
                rss_url
            )

            count = len(feed.entries)

            print(
                f"   Found: {count}"
            )

            if count == 0:
                continue

            for entry in feed.entries[:20]:

                title = getattr(
                    entry,
                    "title",
                    ""
                ).strip()

                link = getattr(
                    entry,
                    "link",
                    ""
                ).strip()

                if not title:
                    continue

                if not link:
                    continue

                all_news.append({
                    "title": title,
                    "link": link,
                    "published": getattr(
                        entry,
                        "published",
                        ""
                    ),
                    "source": source_name
                })

            time.sleep(0.3)

        except Exception as e:

            print(
                f"   ERROR: {e}"
            )

            continue

    return all_news
