import telebot
from tcp import send_tcp_request

bot = telebot.TeleBot("token", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['move'])
def move_engine(message):
    res = send_tcp_request('up')
    bot.reply_to(message, res)

bot.infinity_polling()