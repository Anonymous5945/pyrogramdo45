import time
from pyrogram import Client, filters

from pyrobot.pyrobot import PyroBot

from pyrobot import TG_URI


async def get_banr_command(message):
   for member in message.left_chat_member:
        try:
              await message.chat.kick_member(
                  user_id=member.id
              )
        except Exception as error:
            await message.reply_text(
                str(error)
            )
@PyroBot.on_message(filters.chat(chats=TG_URI) & filters.left_chat_member)
async def autor_ban(_, message):
       await get_banr_command(message)
