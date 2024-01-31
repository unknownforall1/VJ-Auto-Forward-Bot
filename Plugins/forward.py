# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
            func = message.copy if Config.AS_COPY else message.forward
            await func(int(to_channel), Config.AS_COPY)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(1)
   except Exception as e:
      logger.exception(e)


@channelforward.on_message()
def promote_user(client, message):
    if message.reply_to_message and message.reply_to_message.from_user.id != client.get_me().id and message.from_user.id == owner_id:
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        client.promote_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True
        )
