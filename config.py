import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "")

# RSS Sources
RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "Wired": "https://www.wired.com/feed/rss",
    "Hacker News": "https://hnrss.org/frontpage"
}

# App Settings
CHECK_INTERVAL = 300      # 5 minutes
NEWS_RETENTION_HOURS = 48
SIMILARITY_THRESHOLD = 92

# Timer Settings
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "5"))  # تعداد خبرهای ارسالی در هر دور
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", "5"))  # فاصله بین دورها

# AI Settings
ENABLE_AI_AGENT = os.getenv("ENABLE_AI_AGENT", "False").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")

# Post Format Settings
POST_FORMAT = {
    "show_image": os.getenv("SHOW_IMAGE", "True").lower() == "true",
    "show_title": os.getenv("SHOW_TITLE", "True").lower() == "true",
    "show_category": os.getenv("SHOW_CATEGORY", "True").lower() == "true",
    "show_summary": os.getenv("SHOW_SUMMARY", "True").lower() == "true",
    "show_source": os.getenv("SHOW_SOURCE", "True").lower() == "true",
    "show_link": os.getenv("SHOW_LINK", "True").lower() == "true",
    "show_channel_tag": os.getenv("SHOW_CHANNEL_TAG", "True").lower() == "true",
    "summary_paragraphs": int(os.getenv("SUMMARY_PARAGRAPHS", "2")),
    "order": [
        "category",
        "image",
        "title",
        "summary",
        "source",
        "link",
        "channel_tag"
    ]
}

# AI Analysis Keywords
MIDDLE_EAST_KEYWORDS = [
    "iran",
    "israel",
    "gaza",
    "lebanon",
    "syria",
    "middle east",
    "saudi",
    "iraq",
    "jordan",
    "yemen",
    "palestine",
]
