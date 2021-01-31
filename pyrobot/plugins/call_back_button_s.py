#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from pyrogram.types import (
    CallbackQuery
)
from pyrobot.pyrobot import PyroBot
from pyrobot.helper_functions.you_tube_dl_button import youtube_dl_call_back
from pyrobot.helper_functions.warn_hlprs.remove_warn import remove_warn


@PyroBot.on_callback_query()
async def button(client: PyroBot, callback_query: CallbackQuery):
    # NOTE: You should always answer,
    # but we want different conditionals to
    # be able to answer to differnetly
    # (and we can only answer once),
    # so we do always answer here.
    # and, do any heavy processing later!
    cb_data = callback_query.data
    if cb_data == "new-moon-face":
        #await callback_query.message.edit("🎯")
       buttons = []
       button1 = []
       button2 = []
       c=0   
       for i in message.reply_to_message.reply_markup.inline_keyboard:
         for x in i:
          c=c+1
          if c in ((1,2,3,4,5)):
           buttons.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
          elif c in ((6,7,8,9,10)):
           button1.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
          elif c in ((11,12,13,14,15)):
           button2.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
       keyboard = InlineKeyboardMarkup([buttons, button1,button2])
       await message.reply("dan pls dont ban", reply_markup=keyboard)
    elif cb_data.startswith("ytdl_"):
        await callback_query.answer(
            text="please wait, the message will be edited after a SHORT time",
            show_alert=False
        )
        _, call_back_data = cb_data.split("_")
        await youtube_dl_call_back(client, callback_query, call_back_data)

    elif cb_data.startswith("rmwarn_"):
        _c, first_i, second_i = cb_data.split("_")
        await remove_warn(client, callback_query, str(first_i), int(second_i))
