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
@# Import the necessary modules
from pyrogram import Client, filters
from pyrogram.types import ChatMember, ChatPermissions

# Add an admin to the group
from pyrogram import Client, filters
@channelforward.on_message(filters.command("add_admin", prefixes="/"))
def add_admin(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    client.promote_chat_member(chat_id, user_id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)

@channelforward.on_message(filters.command("give_title", prefixes="/"))
def give_title(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    client.set_administrator_title(chat_id, user_id, "Pro")
