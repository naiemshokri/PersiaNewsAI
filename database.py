import sqlite3
from pathlib import Path

DB_DIR = Path("data")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "news.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,
        link TEXT UNIQUE NOT NULL,

        source TEXT,
        published_at TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_news(title, link, source, published_at):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO news
        (title, link, source, published_at)
        VALUES (?, ?, ?, ?)
        """, (
            title,
            link,
            source,
            published_at
        ))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def count_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM news"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def cleanup_old_news(hours=48):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""
        DELETE FROM news
        WHERE created_at <
        datetime('now', '-{hours} hours')
        """
    )

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted
