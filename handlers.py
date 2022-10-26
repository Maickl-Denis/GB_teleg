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


def chese_Game(num1, num2, call):
    if call.data[1:2] == 'b':
        game.call_data_bot(num1, num2, call=call, id_user=int(call.data[2:]))
    else:
        game.call_data(num1, num2, call=call, id_pair=int(call.data[1:]))


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
    bot.send_message(message.chat.id, text="Привет, чем будем заниматься", reply_markup=keyboards.inline_menu_start)

#перехват команд от кнопок
calc_result = ''
@bot.callback_query_handler(func=lambda call: True)
def OS_but(call):
    global calc_result
    if call.data == 'g_go':
        logining(call, "Вход в Игры")
        bot.send_message(call.message.chat.id, text="С кем вы бедете играть в игру")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=keyboards.inline_menu_game)
    if call.data == 'g_human':
        game.main(call, 1)
        logining(call, "Выбрана игра с человеком")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == 'g_bot':
        game.main(call, 0)
        logining(call, "Выбрана игра с Ботом")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == 'calc':
        logining(call, "Калькулятор")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=keyboards.inline_menu_calc)
    if call.data == 'calc_1':
        calc_result +='1'
        logining(call, "1")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_2':
        calc_result +='2'
        logining(call, "2")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_3':
        calc_result +='3'
        logining(call, "3")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_4':
        calc_result +='4'
        logining(call, "4")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_5':
        calc_result +='5'
        logining(call, "5")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_6':
        calc_result +='6'
        logining(call, "6")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_7':
        calc_result +='7'
        logining(call, "7")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_8':
        calc_result +='8'
        logining(call, "8")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_9':
        calc_result +='9'
        logining(call, "9")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_0':
        calc_result +='0'
        logining(call, "0")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_+':
        calc_result += '+'
        logining(call, "+")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_-':
        calc_result += '-'
        logining(call, "-")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_*':
        calc_result += '*'
        logining(call, "*")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_/':
        calc_result += '/'
        logining(call, "/")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_(':
        calc_result += '('
        logining(call, "(")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_)':
        calc_result += ')'
        logining(call, ")")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_.':
        calc_result += '.'
        logining(call, ".")
        bot.answer_callback_query(call.id, show_alert=False, text=calc_result)
    if call.data == 'calc_=':
        try:
            bot.send_message(call.message.chat.id, text=f"{calc_result} = {eval(calc_result)}")
            bot.answer_callback_query(call.id, '')
            logining(call, f"{calc_result} = {eval(calc_result)}")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        except:
            bot.send_message(call.message.chat.id, text=f"{calc_result} - это посчитать невозможно")
            bot.answer_callback_query(call.id, '')
            logining(call, calc_result)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        calc_result = ''
    if call.data[:1] == '1':
        chese_Game(0,0,call)
    if call.data[:1] == '2':
        chese_Game(0, 1, call)
    if call.data[:1] == '3':
        chese_Game(0, 2, call)
    if call.data[:1] == '4':
        chese_Game(1, 0, call)
    if call.data[:1] == '5':
        chese_Game(1, 1, call)
    if call.data[:1] == '6':
        chese_Game(1, 2, call)
    if call.data[:1] == '7':
        chese_Game(2, 0, call)
    if call.data[:1] == '8':
        chese_Game(2, 1, call)
    if call.data[:1] == '9':
        chese_Game(2, 2, call)
    if call.data == "win":
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

####Эхо ответ
@bot.message_handler(content_types=['text'])
def echo(message):
    print(f"{data()} -", message.from_user.id, message.from_user.first_name,
          message.from_user.last_name, "написал", {message.text})
    text = f"Привет, ты написал: {message.text}"
    bot.reply_to(message, text=text)