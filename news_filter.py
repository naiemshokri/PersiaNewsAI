TECH_KEYWORDS = [

    "ai",
    "openai",
    "anthropic",
    "google",
    "meta",
    "apple",
    "microsoft",
    "tesla",
    "spacex",

    "startup",
    "funding",
    "venture",

    "robot",
    "robotaxi",

    "cyber",
    "security",
    "hack",

    "chip",
    "gpu",
    "nvidia",

    "telegram",

    "gpt",
    "llm",

    "android",
    "iphone",
    "ios",

    "technology",
    "tech"
]


def is_good_news(title):

    title = title.lower()

    for keyword in TECH_KEYWORDS:

        if keyword in title:
            return True

    return False
