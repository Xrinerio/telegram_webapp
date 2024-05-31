import os

from telebot import types
import telebot

bot = telebot.TeleBot('7387733428:AAFuiERyYj0VfqUXLxA5zrpf4PSEMP1laME   ')

def webAppKeyboard(): 
   keyboard = types.ReplyKeyboardMarkup(row_width=1) 
   webAppTest = types.WebAppInfo("index.html") 
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) 
   keyboard.add(one_butt)

   return keyboard 

def webAppKeyboardInline():
   keyboard = types.InlineKeyboardMarkup(row_width=1) 
   webApp = types.WebAppInfo("https://telegram.mihailgok.ru")
   one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp)
   keyboard.add(one)

   return keyboard


@bot.message_handler(commands=['start'])
def start_fun(message):
   bot.send_message( message.chat.id, 'Абубибас', parse_mode="Markdown", reply_markup=webAppKeyboard())


@bot.message_handler(content_types="text")
def new_mes(message):
   start_fun(message)


@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
   print(webAppMes) #вся информация о сообщении
   print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
   bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}") 
   #отправляем сообщение в ответ на отправку данных из веб-приложения 

if __name__ == '__main__':
   bot.infinity_polling()