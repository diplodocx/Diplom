import telebot
from tcp import send_tcp_request
from db import insert_action_data, get_command
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def act(button_name, param, call, action_type_id):
    insert_action_data(action_type_id)
    command = get_command(button_name, param)
    res = send_tcp_request(f'{command[0]}, {command[1]}')
    bot.send_message(call.message.chat.id, res)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)  # Создаем клавиатуру с двумя кнопками в строке
    btn_1 = types.InlineKeyboardButton("Этаж 1", callback_data='button_1')
    btn_2 = types.InlineKeyboardButton("Этаж 2", callback_data='button_2')
    btn_3 = types.InlineKeyboardButton("Этаж 3", callback_data='test')
    keyboard.add(btn_1, btn_2, btn_3)  # Добавляем кнопки на клавиатуру
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)  # Отправляем сообщение с клавиатурой


@bot.callback_query_handler(func=lambda call: True)  # Обработчик для callback-запросов
def callback_inline(call):
    insert_action_data(1)
    if call.data == 'button_1':
        act(call.data, 'up', call, 1)
    elif call.data == 'button_2':
        act(call.data, 'up', call, 1)
    elif call.data == 'test':
        act(call.data, 'up', call, 1)


bot.infinity_polling()
