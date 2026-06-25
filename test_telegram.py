import asyncio

from telegram_bot import send_message


async def main():

    await send_message(
        "🚀 PersiaNews AI Online\n\nFirst Telegram Test"
    )


asyncio.run(main())
