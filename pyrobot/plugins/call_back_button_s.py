#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from pyrogram.types import (
    CallbackQuery
)
from pyrobot.pyrobot import PyroBot
from pyrobot.helper_functions.you_tube_dl_button import youtube_dl_call_back
from pyrobot.helper_functions.warn_hlprs.remove_warn import remove_warn
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import time
from datetime import datetime

@PyroBot.on_callback_query()
async def button(client: PyroBot, callback_query: CallbackQuery):
    # NOTE: You should always answer,
    # but we want different conditionals to
    # be able to answer to differnetly
    # (and we can only answer once),
    # so we do always answer here.
    # and, do any heavy processing later!
   cb_data = callback_query.data
   if callback_query.message.from_user.id == callback_query.reply_to_message.from_user.id:
    f_text=""
    u=callback_query.message.caption[57:58]
    u=int(u)
    n=callback_query.message.caption[72:73]
    n=int(n)
    if u > 0 and cb_data in (("count 1","count 2","count 3","count 4","count 5","count 6")):
      text= callback_query.message.caption[0:56]
      uo=str(u)
      n=n+1
      no=str(n)
      f_text = f"{text}\n{uo} attempt left\n{no} found"
    elif u <= 1 and cb_data not in (("count 1","count 2","count 3","count 4","count 5","count 6")):
     u=0
     await callback_query.message.delete()
     rm=InlineKeyboardMarkup([[InlineKeyboardButton("Join Dramaost",url = "http://t.me/DramaOST") ] ])
     id=callback_query.from_user.username or callback_query.from_user.first_name
     m1 = f"<a href='tg://user?id={callback_query.from_user.id}'>{id}</a>"
     t=f"{m1},\nyou have failed this Group. As a rightful citizen of this group I'm muting you for 5 minutes\n                                       ~ Green Arrow"
     await client.send_photo(
        callback_query.message.chat.id,'/app/arrow.jpg',
        caption=t,
        reply_markup=rm)
    else:
     text= callback_query.message.caption[0:56]
     u=u-1
     uo=str(u)
     no=str(n)
     f_text = f"{text}\n{uo} attempt left\n{no} found"
    if u > 0 and n <= 6:
     buttons = []
     button1 = []
     button2 = []
     button3 = []
     button4 = []
     c=0
     keyboard = InlineKeyboardMarkup([buttons, button1,button2,button3,button4])
     for i in callback_query.message.reply_markup.inline_keyboard:
      for x in i:
        c=c+1
        if x.callback_data.split(':')[-1] == cb_data and cb_data in (("count 1","count 2","count 3","count 4","count 5","count 6")):
         if c in range(1,9):
           buttons.append(InlineKeyboardButton(str('✅'), callback_data='yes'))
         elif c in range(9,17):
           button1.append(InlineKeyboardButton(str('✅'), callback_data='yes'))
         elif c in range(17,25):
           button2.append(InlineKeyboardButton(str('✅'), callback_data='yes'))
         elif c in range(25,33):
           button3.append(InlineKeyboardButton(str('✅'), callback_data='yes'))
         elif c in range(33,41):
           button4.append(InlineKeyboardButton(str('✅'), callback_data='yes'))
        elif x.callback_data.split(':')[-1] == cb_data and cb_data not in (("count 1","count 2","count 3","count 4","count 5","count 6")):
         if c in range(1,9):
           buttons.append(InlineKeyboardButton(str('❌'), callback_data='no'))
         elif c in range(9,17):
           button1.append(InlineKeyboardButton(str('❌'), callback_data='no'))
         elif c in range(17,25):
           button2.append(InlineKeyboardButton(str('❌'), callback_data='no'))
         elif c in range(25,33):
           button3.append(InlineKeyboardButton(str('❌'), callback_data='no'))
         elif c in range(33,41):
           button4.append(InlineKeyboardButton(str('❌'), callback_data='no'))
        else:
         if c in range(1,9):
           buttons.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
         elif c in range(9,17):
           button1.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
         elif c in range(17,25):
           button2.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
         elif c in range(25,33):
           button3.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
         elif c in range(33,41):
           button4.append(InlineKeyboardButton(str(x.text.split(':')[-1]), callback_data=x.callback_data.split(':')[-1]))
     await callback_query.edit_message_text(
         text=f_text,
         reply_markup=keyboard
        )
    if u > 0 and n >=6:
      U1=callback_query.message.date
      W1=time.time()
      a1=datetime.fromtimestamp(U1).strftime("%Y.%m.%d %H:%M:%S")
      b1=datetime.fromtimestamp(W1).strftime("%Y.%m.%d %H:%M:%S")
      d1 = datetime.strptime(a1, "%Y.%m.%d %H:%M:%S")
      d2 = datetime.strptime(b1, "%Y.%m.%d %H:%M:%S")
      go = (d2-d1)
      if u == 2:
        nom="first"
      else:
         nom="second"
      await callback_query.message.delete()
      rm=InlineKeyboardMarkup([[InlineKeyboardButton("Join Dramaost",url = "http://t.me/DramaOST" )]])
      id=callback_query.from_user.username or callback_query.from_user.first_name
      m1 = f"<a href='tg://user?id={callback_query.from_user.id}'>{id}</a>"
      t=f"hi {m1}\n\nWelcome to {callback_query.message.chat.title} Group\n\n user id : {callback_query.from_user.id}\n\nCongos !!! you have completed task in {nom} attempt ( in {go})"
      await client.send_photo(
        callback_query.message.chat.id,'/app/welcome.jpg',
        caption=t,
        reply_markup=rm)
    
   if cb_data.startswith("ytdl_"):
        await callback_query.answer(
            text="please wait, the message will be edited after a SHORT time",
            show_alert=False
        )
        _, call_back_data = cb_data.split("_")
        await youtube_dl_call_back(client, callback_query, call_back_data)

   elif cb_data.startswith("rmwarn_"):
        _c, first_i, second_i = cb_data.split("_")
        await remove_warn(client, callback_query, str(first_i), int(second_i))
