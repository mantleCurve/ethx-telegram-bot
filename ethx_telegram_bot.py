import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
from scrapy import Selector

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def sell_price():
    r = requests.get('https://ethx.in')
    sel = Selector(text=r.content)
    sell_price = sel.xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[2]/a/text()').extract()[0]
    return sell_price

def buy_price():
    r = requests.get('https://ethx.in')
    sel = Selector(text=r.content)
    buy_price = sel.xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[1]/a/text()').extract()[0]
    return buy_price

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    markup = ReplyKeyboardMarkup(keyboard=[
                     [KeyboardButton(text='Buy Price')],
                     [KeyboardButton(text='Sell Price')],
                 ])
    message = msg['text']
    if message=="/start":
        bot.sendMessage(chat_id, 'Get Etherium prices from ETHX.IN', reply_markup=markup)
    
    if message=="Buy Price":
        bot.sendMessage(chat_id, buy_price(), reply_markup=markup)
    if message=="Sell Price":
        bot.sendMessage(chat_id, sell_price(), reply_markup=markup)


def on_callback_query(msg):
    print (msg)
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Got it')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
