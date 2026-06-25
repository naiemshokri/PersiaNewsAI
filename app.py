import asyncio

from rss import fetch_all_news

from database import (
    init_db,
    save_news,
    count_news,
    cleanup_old_news
)

from dashboard import (
    show_dashboard,
    log_event
)

from telegram_bot import send_message

from scheduler import wait_next_cycle

from category_engine import detect_category
from formatter import format_post

from news_filter import is_good_news


MAX_NEWS_PER_RUN = 5


async def run_once():

    init_db()

    deleted = cleanup_old_news(24)

    if deleted:

        log_event(
            f"[CLEANUP] Removed {deleted} old news"
        )

    news_list = fetch_all_news()

    published = 0
    duplicates = 0
    errors = 0

    show_dashboard(
        feeds=11,
        collected=len(news_list),
        published=0,
        duplicates=0,
        errors=0
    )

    for news in news_list:

        if published >= MAX_NEWS_PER_RUN:
            break

        try:

            if not is_good_news(
                news["title"]
            ):
                continue

            saved = save_news(
                title=news["title"],
                link=news["link"],
                source=news["source"],
                published_at=news["published"]
            )

            if not saved:

                duplicates += 1
                continue

            category = detect_category(
                news["title"]
            )

            message = format_post(
                title=news["title"],
                category=category,
                source=news["source"],
                link=news["link"]
            )

            await send_message(message)

            published += 1

            log_event(
                f"[PUBLISHED] {news['title'][:60]}"
            )

        except Exception as e:

            errors += 1

            log_event(
                f"[ERROR] {e}"
            )

    show_dashboard(
        feeds=len(RSS_FEEDS),
        collected=len(news_list),
        published=published,
        duplicates=duplicates,
        errors=errors
    )

    print()
    print("=" * 50)
    print("Published :", published)
    print("Duplicates:", duplicates)
    print("Database  :", count_news())
    print("=" * 50)
    print()


async def main():

    print("=" * 50)
    print("PersiaNews AI Starting...")
    print("=" * 50)

    while True:

        await run_once()

        wait_next_cycle(15)


if __name__ == "__main__":

    asyncio.run(main())
