from pyrogram import filters
from pyrogram.types import Message
from pyrobot.helper_functions.admin_check import admin_check
from pyrobot.helper_functions.cust_p_filters import (
    admin_fliter,
    sudo_filter
)

@PyroBot.on_message(filters.regex("(?i)@admin(s)?"))
async def tag_admins(client: PyroBot, m: Message):

    adminslist = []

    if m.chat.type in ("supergroup", "group"):
        async for member in c.iter_chat_members(m.chat.id, filter="administrators"):
            adminslist.append(member.user.id)

        if m.from_user.id in adminslist:
            # Don't work if called by an admin himself and log this!
            return

        mentions = "**{}** Admins, here!!!"
        admin_count = 0

        async for a in alladmins:
            if a.user.is_bot:
                pass
            else:
                admin_count += 1
                adminid = a.user.id
                mentions += f"[\u2063](tg://user?id={adminid})"

        text = mentions.format(admin_count)
        text += f"\n[{m.from_user.first_name}](tg://user?id={m.from_user.id}) is calling you!"
        await m.reply_text(text, parse_mode="markdown")

    else:
        await m.reply_text(
            "`It doesn't work here ¯\_(ツ)_/¯`",
            parse_mode="markdown",
            reply_to_message_id=m.message_id,
        )

    return
