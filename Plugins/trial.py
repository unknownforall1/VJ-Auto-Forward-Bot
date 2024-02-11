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
# Import the necessary modules
from pyrogram import Client, filters
from pyrogram.types import ChatMember, ChatPermissions

# Add an admin to the group
from pyrogram import Client, filters
import time

@channelforward.on_message(filters.edited & filters.group)
def delete_message(client, message):
    time.sleep(300)  # 300 seconds = 5 minutes
    client.delete_messages(message.chat.id, message.message_id)
