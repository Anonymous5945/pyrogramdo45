from pyrogram import Client, filters

@Client.on_message(filters.linked_channel & filters.incoming)
async def autopin(client, message):
    await message.unpin_chat_message(
    Message.chat.id
    )
