import telebot
from tcp import send_tcp_request
from db import insert_action_data, get_command
from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['move'])
def move_engine(message):
    insert_action_data(1)
    command = get_command('test', 'up')
    res = send_tcp_request(f'{command[0]}, {command[1]}')
    bot.reply_to(message, res)


bot.infinity_polling()
