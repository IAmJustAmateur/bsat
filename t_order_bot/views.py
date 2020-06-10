from django.shortcuts import render
from django.http import HttpResponse

import os
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint

# Create your views here.

def on_chat_message(msg):
    # global bot
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text='Press me', callback_data = 'press')],
    ])
    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard, text='from on_chat_message')

def on_callback_query(msg):
    # global bot
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('CallbackQuery:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)

def index(request):
    
    bot = telepot.Bot(os.environ.get("BOT_TOKEN"))
    MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread() 
    print('Listening...')

    while True:
        time.sleep(1)

    #updates = t_bot()
    return HttpResponse("Hello World! <br> From t_order_bot<br>")

