import time
from pyrogram import Client, filters

from pyrobot.pyrobot import PyroBot

from pyrobot import TG_URI


@PyroBot.on_message(filters.chat(chats=TG_URI) & filters.left_chat_member)
async def banr_fn(client,message):
   for member in message.left_chat_member:
        try:
              await message.chat.kick_member(
                  user_id=member.id
              )
        except Exception as error:
            await message.reply_text(
                str(error)
            )
