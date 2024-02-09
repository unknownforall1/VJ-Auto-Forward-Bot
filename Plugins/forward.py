# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)
owner_id = 6134091518
import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 


from re import escape
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media import message
from pyrogram import filters
from pyrogram.types import Message




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

@channelforward.on_message(filters.command('kick'))
def kick(_, message):
    reply = message.reply_to_message
    if is_admin(message.chat.id, message.from_user.id) and reply:
        bot.kick_chat_member(message.chat.id,
                             message.reply_to_message.from_user.id)
        bot.unban_chat_member(message.chat.id,
                              message.reply_to_message.from_user.id)
        message.reply('kicked @{} !'.format(
            message.reply_to_message.from_user.username))
    elif reply.from_user.id == 6134091518:
        message.reply('This Person is my owner!')
    else:
        message.reply('You are not admin')
        
