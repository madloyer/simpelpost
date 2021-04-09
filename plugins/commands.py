import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_message(filters.private & filters.command(['start']))
async def start(bot, update) :
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TXT.format(
                update.from_user.first_name)
        parse_mode="html")
        