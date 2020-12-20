from pyrogram import Client, filters

@Client.on_message(filters.linked_channel)
async def autopin(Client, Message):
    await Client.unpin_chat_message(
    Message.chat.id
    )
