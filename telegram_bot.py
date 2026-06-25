from telegram import Bot
from telegram.constants import ParseMode

from config import (
    BOT_TOKEN,
    CHANNEL_USERNAME
)

bot = Bot(
    token=BOT_TOKEN
)


async def send_message(text):

    await bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False
    )
