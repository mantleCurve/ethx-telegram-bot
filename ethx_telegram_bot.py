import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
from scrapy import Selector

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def eth_price():
    r = requests.get('https://ethx.in')
    sel = Selector(text=r.content)
    eth_price = sel.xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[2]/a/text()').extract()[0]
    return eth_price

def bit_price():
    r = requests.get('https://ethx.in')
    sel = Selector(text=r.content)
    bit_price = sel.xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[1]/a/text()').extract()[0]
    return bit_price

def ltc_price():
    r = requests.get('https://ethx.in')
    sel = Selector(text=r.content)
    ltc_price = sel.xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[3]/a/text()').extract()[0]
    return ltc_price

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    markup = ReplyKeyboardMarkup(keyboard=[
                     [KeyboardButton(text='Bitcoin Price')],
                     [KeyboardButton(text='Etherium Price')],
                      [KeyboardButton(text='Litcoin Price')],
                 ])
    message = msg['text']
    if message=="/start":
        bot.sendMessage(chat_id, 'Get crypto prices from ETHX.IN', reply_markup=markup)
    
    if message=="Bitcoin Price":
        bot.sendMessage(chat_id, bit_price(), reply_markup=markup)
    if message=="Etherium Price":
        bot.sendMessage(chat_id, eth_price(), reply_markup=markup)
    if message=="Litcoin Price":
        bot.sendMessage(chat_id, ltc_price(), reply_markup=markup)


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
