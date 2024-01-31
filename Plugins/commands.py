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


admins = {}
ban_counts = {}
group_id = "-1002122236310"

def ban_user(admin_id, user_id):
    if admin_id in ban_counts:
        ban_counts[admin_id] += 1
        if ban_counts[admin_id] >= 5:
            for admin in admins:
                channelforward.promote_chat_member(
                    chat_id=group_id,
                    user_id=admin,
                    can_change_info=False,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_delete_messages=False,
                    can_invite_users=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False
                )
            channelforward.send_message(
                chat_id=group_id,
                text="All admins have been dismissed due to excessive banning."
            )

    else:
        ban_counts[admin_id] = 1
    admins[user_id] = admin_id

