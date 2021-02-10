from pyrogram import filters
import os
from PIL import Image
import random
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (
    Message
)
from pyrobot import COMMAND_HAND_LER

from pyrobot.pyrobot import PyroBot

@PyroBot.on_message(
    filters.command(["playgame", "play"], COMMAND_HAND_LER)
)
async def user_fn(client: PyroBot, message: Message):
    H=[('🎲', 'game-die', 'game-die.png'), ('🎯', 'direct hit', 'direct hit.png'), ('⚽', 'soccer ball', 'soccer ball.png'), ('🥎', 'softball', 'softball.png'), ('🎪', 'circus tent', 'circus tent.png'), ('🎬', 'clapper board', 'clapper board.png'), ('🎹', 'musical keyboard', 'musical keyboard.png'), ('🎤', 'microphone', 'microphone.png'), ('🎭', 'performing arts', 'performing arts.png'), ('🎰', 'slot machine', 'slot machine.png'), ('🙉', 'hear-no-evil', 'hear-no-evil.png'), ('🦊', 'fox', 'fox.png'), ('🐖', 'pig', 'pig.png'), ('🐍', 'snake', 'snake.png'), ('🌹', 'rose', 'rose.png'), ('🧲', 'magnet', 'magnet.png'), ('🛸', 'flying saucer', 'flying saucer.png'), ('🌟', 'glowing star', 'glowing star.png'), ('🎄', 'christmas tree', 'christmas tree.png'), ('🎁', 'wrapped', 'wrapped.png'), ('🍪', 'cookie', 'cookie.png'), ('👀', 'eyes', 'eyes.png'), ('👌', 'ok hand', 'ok hand.png'), ('👻', 'ghost', 'ghost.png'), ('😈', 'devil', 'devil.png'), ('🌚', 'new-moon-face', 'new-moon-face.png'), ('🐬', 'dolphin', 'dolphin.png'), ('🧴', 'lotion-bottle', 'lotion-bottle.png'), ('🖲', 'trackball', 'trackball.png'), ('🥢', 'chopsticks', 'chopsticks.png'), ('🍼', 'baby-bottle', 'baby-bottle.png'), ('🕸', 'spider-web', 'spider-web.png'), ('💳', 'credit card', 'credit card.png'), ('🛏', 'bed', 'bed.png'), ('🎎', 'japanese-dolls', 'japanese-dolls.png'), ('🌧', 'cloud-with-rain', 'cloud-with-rain.png'), ('🛒', 'shopping-cart', 'shopping-cart.png'), ('📄', 'page-facing-up', 'page-facing-up.png'), ('📚', 'books', 'books.png'), ('😝', 'guide', 'guide.png')]
    sam=random.sample(H,6)
    a1= sam[0]
    a2= sam[1]
    a3= sam[2]
    a4= sam[3]
    a5= sam[4]
    a6= sam[5]
    random.shuffle(H)
    ao1 = 'emojis/' + a1[2]
    ab1 = Image.open(ao1, 'r')
    ao2 = 'emojis/' + a2[2]
    ab2 = Image.open(ao2, 'r')
    ao3 = 'emojis/' + a3[2]
    ab3 = Image.open(ao3, 'r')
    ao4 = 'emojis/' + a4[2]
    ab4 = Image.open(ao4, 'r')
    ao5 = 'emojis/' + a5[2]
    ab5 = Image.open(ao5, 'r')
    ao6 = 'emojis/' + a6[2]
    ab6 = Image.open(ao6, 'r')
    filename1 = 'emojis/h.jpg'
    bg = Image.open(filename1, 'r')
    text_img = Image.new('RGBA', (640,640), (0, 0, 0, 0))
    text_img.paste(bg, (0,0))
    text_img.paste(ab1, (0,120), mask=ab1)
    text_img.paste(ab2, (120,280), mask=ab2)
    text_img.paste(ab3, (400,160), mask=ab3)
    text_img.paste(ab4, (500,300), mask=ab4)
    text_img.paste(ab5, (320,360), mask=ab5)
    text_img.paste(ab6, (200,80), mask=ab6)
    text_img.save("ball.png", format="png")
    buttons = []
    buttons1 = []
    buttons2 = []
    buttons3 = []
    buttons4 = []
    a , b , b1= zip(*H)
    c=0
    po=0
    for i,j in zip(a,b):
     c=c+1
     if j in ((a1[1],a2[1],a3[1],a4[1],a5[1],a6[1])):
         po=po+1
         j=f"count {po}"
         if c in range(1,9):
           buttons.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(9,17):
           buttons1.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(17,25):
           buttons2.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(25,33):
           buttons3.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(33,41):
          buttons4.append(InlineKeyboardButton(str(i),callback_data=j))
     else:
         if c in range(1,9):
           buttons.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(9,17):
           buttons1.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(17,25):
           buttons2.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(25,33):
           buttons3.append(InlineKeyboardButton(str(i),callback_data=j))
         elif c in range(33,41):
          buttons4.append(InlineKeyboardButton(str(i),callback_data=j))

    keyboard = InlineKeyboardMarkup([buttons,buttons1,buttons2,buttons3,buttons4])
    t=f"Complete the task by selecting Emoji shown in above pic\n\n2 attempt left\n0 found"
    await client.send_photo(
        message.chat.id,'ball.png',
        caption=t,
        reply_markup=keyboard)
    os.remove("ball.png")

     
