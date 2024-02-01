from pyrogram import Client
import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.group & filters.admins)
def reply_hi_to_admin(client, message):
    client.send_message(message.chat.id, "hi")
