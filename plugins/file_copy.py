from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import Config
import asyncio


@Client.on_message(filters.channel & filters.all)
async def copy(bot, message):
    try:
        await message.copy(
            chat_id=Config.TO_CHANNEL
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        print(e)
        pass
