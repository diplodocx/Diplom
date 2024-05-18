import telebot
from telebot import types

from config import TOKEN
from db import insert_action_data, get_command
from tcp import send_tcp_request
from speech_encoder import recognize

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def act(button_name, param, call, action_type_id):
    insert_action_data(action_type_id)
    command = get_command(button_name, param)
    res = send_tcp_request(f'{command[0]}{command[1]}')
    bot.send_message(call.message.chat.id, res)


def voice_act(button_name, param, message, action_type_id):
    insert_action_data(action_type_id)
    command = get_command(button_name, param)
    res = send_tcp_request(f'{command[0]}{command[1]}')
    bot.send_message(message.chat.id, res)


@bot.message_handler(content_types=['voice'])
def process_audio(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('tmp.wav', 'wb') as new_file:
        new_file.write(downloaded_file)
    text = recognize()
    if 'этаж' in text:
        if '2' in text:
            voice_act('button_2', '02', message, 1)


@bot.message_handler(commands=['move'])
def move(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)  # Создаем клавиатуру с двумя кнопками в строке
    btn_1 = types.InlineKeyboardButton("Этаж 1", callback_data='button_1')
    btn_2 = types.InlineKeyboardButton("Этаж 2", callback_data='button_2')
    btn_3 = types.InlineKeyboardButton("Этаж 3", callback_data='test')
    keyboard.add(btn_1, btn_2, btn_3)  # Добавляем кнопки на клавиатуру
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)  # Отправляем сообщение с клавиатурой


@bot.message_handler(commands=['light'])
def light(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)  # Создаем клавиатуру с двумя кнопками в строке
    btn_1 = types.InlineKeyboardButton("Лампочка 1 выкл", callback_data='button_3')
    btn_2 = types.InlineKeyboardButton("Лампочка 1 вкл", callback_data='button_4')
    btn_3 = types.InlineKeyboardButton("Лампочка 3", callback_data='test')
    keyboard.add(btn_1, btn_2, btn_3)  # Добавляем кнопки на клавиатуру
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)  # Отправляем сообщение с клавиатурой


@bot.callback_query_handler(func=lambda call: True)  # Обработчик для callback-запросов
def callback_inline(call):
    insert_action_data(1)
    if call.data == 'button_1':
        act(call.data, '01', call, 1)
    elif call.data == 'button_2':
        act(call.data, '02', call, 1)
    elif call.data == 'button_3':
        act(call.data, '00', call, 2)
    elif call.data == 'button_4':
        act(call.data, '00', call, 2)
    elif call.data == 'test':
        act(call.data, '00', call, 1)


bot.infinity_polling()
