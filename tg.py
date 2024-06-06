import os

from telebot import types
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))

def webAppKeyboard(): 
   keyboard = types.ReplyKeyboardMarkup(row_width=1) 
   webAppTest = types.WebAppInfo("site") 
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) 
   keyboard.add(one_butt)

   return keyboard 

def webAppKeyboardInline():
   keyboard = types.InlineKeyboardMarkup(row_width=1) 
   webApp = types.WebAppInfo("site")
   one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp)
   keyboard.add(one)

   return keyboard


@bot.message_handler(commands=['start'])
def start_fun(message):
   bot.send_message( message.chat.id, 'Абубибас', parse_mode="Markdown", reply_markup=webAppKeyboard())


@bot.message_handler(content_types="text")
def new_mes(message):
   start_fun(message)

if __name__ == '__main__':
   bot.infinity_polling()