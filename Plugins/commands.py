# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

from pyrogram import filters, Client
from bot import channelforward
from config import Config
from translation import Translation

import time

banned_userss = 0
ban_start_time = time.time()

# Assume logic to ban users, and if 5 users are banned within 10 minutes, dismiss the admin
def ban_user():
    global banned_userss
    global ban_start_time
    banned_userss += 1
    if banned_userss == 5 and time.time() - ban_start_time <= 600:
        dismiss_admin()
        
################################################################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text=Translation.START,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################


admins = {}  # Store last ban time for each admin
banned_users = {}  # Store banned users count for each admin

@channelforward.on_message()
def handle_message(client, message):
    if message.from_user.is_admin:
        if message.text == "banned a user":
            if message.from_user.id in admins:
                if time.time() - admins[message.from_user.id] < 600:
                    banned_users[message.from_user.id] = banned_users.get(message.from_user.id, 0) + 1
                    if banned_users[message.from_user.id] >= 5:
                        client.restrict_chat_member(
                            chat_id=message.chat.id,
                            user_id=message.from_user.id,
                            can_restrict_members=False
                        )
            else:
                admins[message.from_user.id] = time.time()
                banned_users[message.from_user.id] = 1

                
