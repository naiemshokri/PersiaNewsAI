def detect_category(title):

    title = title.lower()

    ai_keywords = [
        "ai",
        "openai",
        "chatgpt",
        "gemini",
        "claude",
        "llm",
        "anthropic"
    ]

    startup_keywords = [
        "startup",
        "funding",
        "raised",
        "venture",
        "yc",
        "y combinator"
    ]

    middle_east_keywords = [
        "iran",
        "israel",
        "gaza",
        "lebanon",
        "syria",
        "middle east"
    ]

    if any(word in title for word in ai_keywords):
        return "🤖 #هوش_مصنوعی"

    if any(word in title for word in startup_keywords):
        return "🚀 #استارتاپ"

    if any(word in title for word in middle_east_keywords):
        return "🌍 #خاورمیانه"

    return "💻 #فناوری"
