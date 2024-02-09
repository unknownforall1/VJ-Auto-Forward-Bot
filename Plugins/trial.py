from pyrogram import Client
import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Handler for when bot is added to a group
@channelforwardbot.on_chat_created()
async def send_add_me_button(client, chat):
    if chat.type == "supergroup":
        await client.send_message(
            chat_id=chat.id,
            text=" add our music bot:",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Add Me", url="https://t.me/Sid_Musicbot?startgroup=true")]]
            )
        )
