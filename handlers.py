from main import bot
import datetime
from Config import admin_id
import keyboards
import game

def send_to_admin():
    bot.send_message(chat_id=admin_id, text="Бот запущен\n"
                  "Для запуска меню нажмите /start")
    # print("Telegram бот сборка 005 от 24.05.2022")
    print(data(), "- Бот запущен" )
    bot.infinity_polling()

def data():
    data = datetime.datetime.now()
    return data.strftime('%d-%m-%Y %H:%M')

def logining(call, text):
    print(data(), "- id", call.from_user.id, call.from_user.first_name, call.from_user.last_name, "-", text)

#обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    print(f"{data()} - id", message.from_user.id, message.from_user.first_name,
          message.from_user.last_name, "-", message.text)
    bot.send_message(message.chat.id, text="Хочешь поиграть в крестики нолики", reply_markup=keyboards.inline_menu_start)

#перехват команд от кнопок
calc_result = ''
@bot.callback_query_handler(func=lambda call: True)
def OS_but(call):
    global calc_result
    if call.data == 'g_go':
        logining(call, "Вход в Игры")
        # game.gam_start(call)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == 'calc':
        logining(call, "Калькулятор")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=keyboards.inline_menu_calc)
    if call.data == '1':
        calc_result +='1'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '2':
        calc_result +='2'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '3':
        calc_result +='3'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '4':
        calc_result +='4'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '5':
        calc_result +='5'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '6':
        calc_result +='6'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '7':
        calc_result +='7'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '8':
        calc_result +='8'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '9':
        calc_result +='9'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '0':
        calc_result +='0'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '+':
        calc_result += '+'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '-':
        calc_result += '-'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '*':
        calc_result += '*'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '/':
        calc_result += '/'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '(':
        calc_result += '('
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == ')':
        calc_result += ')'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '.':
        calc_result += '.'
        logining(call, call.data)
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == '=':
        try:
            bot.send_message(call.message.chat.id, text=f"{calc_result} = {eval(calc_result)}")
            bot.answer_callback_query(call.id, '')
            logining(call, call.data)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        except:
            bot.send_message(call.message.chat.id, text=f"{calc_result} = это посчитать невозможно")
            bot.answer_callback_query(call.id, '')
            logining(call, call.data)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        calc_result = ''


####Эхо ответ
@bot.message_handler(content_types=['text'])
def echo(message):
    print(f"{data()} -", message.from_user.id, message.from_user.first_name,
          message.from_user.last_name, "написал", {message.text})
    text = f"Привет, ты написал: {message.text}"
    bot.reply_to(message, text=text)