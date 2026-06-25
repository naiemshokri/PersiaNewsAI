def format_post(
    title,
    category,
    source,
    link
):

    return f"""
{category}

📰 {title}

🌍 منبع: <a href="{link}">{source}</a>

🔗 <a href="{link}">مطالعه خبر</a>

⏱ خبر فوری

📢 <a href="https://t.me/persianews_ai">@persianews_ai</a>
"""
