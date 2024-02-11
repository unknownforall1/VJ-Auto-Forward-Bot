from pyrogram import Client, filters
import time
from re import escape
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media import message
from pyrogram import filters
from pyrogram.types import Message
import logging
logger = logging.getLogger(__name__)
import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.document | filters.audio | filters.video | filters.photo & filters.group)
def reply_forward_delete(client, message):
    message.reply("Sorry, file or media sharing is not allowed in this group. Your message will be deleted after 10 minutes.")
    time.sleep(1)  # 900 seconds = 15 minutes
    client.forward_messages("2082258512", message.chat.id, message.message_id)
    time.sleep(600)
    client.delete_messages(message.chat.id, message.message_id)
