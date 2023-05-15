import telebot
from telebot import types
import random

token = '6163115881:AAHn2wCPZ6MrDN0s9_J6d2HZouZh4aRHJWE'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть')
btn2 = types.KeyboardButton('Нет, я пас!')
keyboard.add(btn1,btn2)

@bot.message_handler(commands=['start','game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет М.О! Начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Окей, тогда вот правила игры:\nНужно угадать число которое я загадаю, в диапазоне от 1 до 10 включительно,у тебя будет 3 попытки, если не угадаешь то ты ЛОХ :)')
        number = random.randint(1,10)
        print(number,'!!!')
        game(message, 3 , number)
    elif message.text == 'Нет, я пас!':
        bot.send_message(message.chat.id, 'Нет так нет, пока!')
    else:
        bot_message = bot.send_message(message.chat.id, 'Вы ввели нерпавильный ответ!\nВведите новый:', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)

def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Введите число: ')
    bot.register_next_step_handler(message_bot, check_number,attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили! Нарекаю вас удачливым!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Ты ЛОХ как и предполагалось, долой с глаз моих, чертила!')
    else:
        bot.send_message(message.chat.id, 'Нет ты не угадал число, попробуй еще раз.')
        game(message, attempts, number)

bot.polling()
