from pyrogram.types import Message
from pyrogram import Client,filters

@Client.on_message(filters.service & filters.incoming)
async def service(client, Message):
    await Message.delete()
