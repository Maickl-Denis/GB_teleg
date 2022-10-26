from main import bot
from telebot import types
from time import sleep as s

id_pair = None
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
user_bot = []
user1 = []
user2 = []
players = []

def check_line(sum_O, sum_X,id_user):
    maps = [user_bot[id_user][1][0][0], user_bot[id_user][1][0][1], user_bot[id_user][1][0][2],
            user_bot[id_user][1][1][0], user_bot[id_user][1][1][1], user_bot[id_user][1][1][2],
            user_bot[id_user][1][2][0], user_bot[id_user][1][2][1], user_bot[id_user][1][2][2]]
    index = [[0,0], [0,1], [0,2],
            [1,0], [1,1], [1,2],
            [2,0], [2,1], [2,2]]
    step = []
    for line in victories:
        o = 0
        x = 0
        for j in line:
            if maps[j] == chr(11093):
                o = o + 1
            if maps[j] == chr(10060):
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in line:
                if maps[j] != chr(11093) and maps[j] != chr(10060):
                    step = index[j]
    return step


def AI(id_user):
    maps = [user_bot[id_user][1][0][0], user_bot[id_user][1][0][1], user_bot[id_user][1][0][2],
            user_bot[id_user][1][1][0], user_bot[id_user][1][1][1], user_bot[id_user][1][1][2],
            user_bot[id_user][1][2][0], user_bot[id_user][1][2][1], user_bot[id_user][1][2][2]]
    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим


    step = check_line(2, 0,id_user=id_user)

    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if not step:
        step = check_line(0, 2,id_user=id_user)

        # 3) если 1 фигура своя и 0 чужих - ставим
    if not step:
        step = check_line(1, 0,id_user=id_user)

    if not step:
        step = check_line(0, 1, id_user=id_user)

        # 4) центр пуст, то занимаем центр
    if not step:
        if maps[4] != chr(10060) and maps[4] != chr(11093):
            step = [1,2]

            # 5) если центр занят, то занимаем первую ячейку
    if not step:
        if maps[0] != chr(10060) and maps[0] != chr(11093):
            step = [0,1]

    return step

def clear_users():
    if not [x for x in [user_id[0] for user_id in user_bot] if x != 0]:
        user_bot.clear()
    if not [x for x in [user_id[0] for user_id in user1] if x != 0]:
        user1.clear()
    if not [x for x in [user_id[0] for user_id in user1] if x != 00]:
        user2.clear()


def call_data(index1, index2, call,id_pair):
    if user2[id_pair][1] != 0 and call.from_user.id in [x[0] for x in user2]:
        if user2[id_pair][2][index1][index2] == '◻':
            user2[id_pair][2][index1][index2] = chr(10060)
            user2[id_pair][1] = 0
            user1[id_pair][1] = 1
            bot.edit_message_reply_markup(user2[id_pair][0], message_id=user2[id_pair][3], reply_markup=make_board(board=user2[id_pair][2], id_pair=id_pair))
            bot.edit_message_reply_markup(user1[id_pair][0], message_id=user1[id_pair][2], reply_markup=make_board(board=user2[id_pair][2], id_pair=id_pair))
            if check_win(user2[id_pair][2])[0] == True or check_win(user2[id_pair][2])[0] == None:
                if check_win(user2[id_pair][2])[0] == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(user1[id_pair][0], message_id=user1[id_pair][2],reply_markup=make_board(end=True, id_pair=id_pair, draw=draw,board=user2[id_pair][2], symbol=check_win(user2[id_pair][2])))
                bot.edit_message_reply_markup(user2[id_pair][0], message_id=user2[id_pair][3],reply_markup=make_board(end=True, id_pair=id_pair, draw=draw, board=user2[id_pair][2],symbol=check_win(user2[id_pair][2])))
                bot.send_message(user1[id_pair][0], 'C кем будете играть?')
                bot.send_message(user2[id_pair][0], 'C кем будете играть?')
                user1[id_pair][0] = 0
                user2[id_pair][0] = 00
                clear_users()
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
    elif user1[id_pair][1] != 0 and call.from_user.id in [x[0] for x in user1]:
        if user2[id_pair][2][index1][index2] == '◻':
            user2[id_pair][2][index1][index2] = chr(11093)
            user1[id_pair][1] = 0
            user2[id_pair][1] = 1
            bot.edit_message_reply_markup(user2[id_pair][0], message_id=user2[id_pair][3], reply_markup=make_board(id_pair=id_pair,board=user2[id_pair][2]))
            bot.edit_message_reply_markup(user1[id_pair][0], message_id=user1[id_pair][2], reply_markup=make_board(id_pair=id_pair,board=user2[id_pair][2]))
            if check_win(user2[id_pair][2])[0] == True or check_win(user2[id_pair][2])[0] == None:
                if check_win(user2[id_pair][2])[0] == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(user1[id_pair][0], message_id=user1[id_pair][2],reply_markup=make_board(end=True, draw=draw,board=user2[id_pair][2], id_pair=id_pair, symbol=check_win(user2[id_pair][2])))
                bot.edit_message_reply_markup(user2[id_pair][0], message_id=user2[id_pair][3],reply_markup=make_board(end=True, draw=draw,board=user2[id_pair][2], id_pair=id_pair,symbol=check_win(user2[id_pair][2])))
                bot.send_message(user1[id_pair][0], 'C кем будете играть?')
                bot.send_message(user2[id_pair][0], 'C кем будете играть?')
                user1[id_pair][0] = 0
                user2[id_pair][0] = 00
                clear_users()


        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
    else:
        bot.answer_callback_query(callback_query_id=call.id, text='Не твой ход! Ожидай соперника!')

def call_data_bot(index1, index2, call,id_user):
    if user_bot[id_user][3] == 0:
        if user_bot[id_user][1][index1][index2] == '◻':
            user_bot[id_user][1][index1][index2] = chr(10060)
            user_bot[id_user][3] = 1
            bot.edit_message_reply_markup(user_bot[id_user][0], message_id=user_bot[id_user][2], reply_markup=make_board_bot(board=user_bot[id_user][1], id=id_user))
            step_bot = AI(id_user)
            if step_bot:
                user_bot[id_user][1][step_bot[0]][step_bot[1]] = chr(11093)
                bot.edit_message_reply_markup(user_bot[id_user][0], message_id=user_bot[id_user][2],reply_markup=make_board_bot(board=user_bot[id_user][1], id=id_user))
                user_bot[id_user][3] = 0
            if check_win(user_bot[id_user][1])[0] == True or check_win(user_bot[id_user][1])[0] == None:
                if check_win(user_bot[id_user][1])[0] == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(user_bot[id_user][0], message_id=user_bot[id_user][2],reply_markup=make_board_bot(end=True, id=id_user, draw=draw,board=user_bot[id_user][1], symbol=check_win(user_bot[id_user][1])))
                bot.send_message(user_bot[id_user][0], 'C кем будете играть?')
                user_bot[id_user][0] = 0
                clear_users()
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
    else:
        bot.answer_callback_query(callback_query_id=call.id, text='Не твой ход!Ожидай!')


def check_win(board):
    for i in range(3):
        if board[i][1] == board[i][0] and board[i][1] == board[i][2] and board[i][1] != '◻':
            return True, board[i][0]
    for i in range(3):
        if board[1][i] == board[0][i] and board[1][i] == board[2][i] and board[1][i] != '◻':
            return True, board[1][i]
    for i in range(2):
        if board[0][0] == board[1][1] and board[1][1] != '◻' and board[1][1] == board[2][2]:
            return True, board[0][0]
        elif board[1][1] != '◻' and board[1][1] == board[0][2] and board[0][2] == board[2][0]:
            return True, board[1][1]
    if board[0][0] != '◻' and board[1][0] != '◻' and board[2][0] != '◻' and board[1][0] != '◻' and board[1][
        1] != '◻' and board[1][2] != '◻' and board[2][0] != '◻' and board[2][1] != '◻' and board[2][2] != '◻':
        return None, None
    return False, False


def make_board(board,id_pair,end=False, draw=False, symbol=chr(10060)):
    if end:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        if draw:
            txt = 'Конец! Ничья!'
        else:
            txt = f'Конец! Победил игрок , который играл за "{symbol[1]}"'
        b1 = types.InlineKeyboardButton(text=txt, callback_data="win")
        keyboard.add(b1)
        return keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text=board[0][0], callback_data=f"1{id_pair}")
    b2 = types.InlineKeyboardButton(text=board[0][1], callback_data=f"2{id_pair}")
    b3 = types.InlineKeyboardButton(text=board[0][2], callback_data=f"3{id_pair}")
    b4 = types.InlineKeyboardButton(text=board[1][0], callback_data=f"4{id_pair}")
    b5 = types.InlineKeyboardButton(text=board[1][1], callback_data=f"5{id_pair}")
    b6 = types.InlineKeyboardButton(text=board[1][2], callback_data=f"6{id_pair}")
    b7 = types.InlineKeyboardButton(text=board[2][0], callback_data=f"7{id_pair}")
    b8 = types.InlineKeyboardButton(text=board[2][1], callback_data=f"8{id_pair}")
    b9 = types.InlineKeyboardButton(text=board[2][2], callback_data=f"9{id_pair}")
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard


def make_board_bot(board,id,end=False, draw=False, symbol=chr(10060)):
    if end:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        if draw:
            txt = 'Конец! Ничья!'
        else:
            txt = f'Конец! Победил игрок , который играл за "{symbol[1]}"'
        b1 = types.InlineKeyboardButton(text=txt, callback_data="win")
        keyboard.add(b1)
        return keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text=board[0][0], callback_data=f"1b{id}")
    b2 = types.InlineKeyboardButton(text=board[0][1], callback_data=f"2b{id}")
    b3 = types.InlineKeyboardButton(text=board[0][2], callback_data=f"3b{id}")
    b4 = types.InlineKeyboardButton(text=board[1][0], callback_data=f"4b{id}")
    b5 = types.InlineKeyboardButton(text=board[1][1], callback_data=f"5b{id}")
    b6 = types.InlineKeyboardButton(text=board[1][2], callback_data=f"6b{id}")
    b7 = types.InlineKeyboardButton(text=board[2][0], callback_data=f"7b{id}")
    b8 = types.InlineKeyboardButton(text=board[2][1], callback_data=f"8b{id}")
    b9 = types.InlineKeyboardButton(text=board[2][2], callback_data=f"9b{id}")
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard

def main(message, flag):
    global user1, user2, players, id_pair, user_bot
    if  flag == 0:
        if message.from_user.id in [user_id[0] for user_id in players]:
            if [user_id[0] for user_id in players].index(message.from_user.id) == 0:
                players.pop([user_id[0] for user_id in players].index(message.from_user.id))
            else:
                players.remove([user_id[0] for user_id in players].index(message.from_user.id))
        user_bot.append([message.from_user.id])
        bot.send_message(message.from_user.id, 'Вы играете с ботом!')
        chat_bot(user_bot.index([message.from_user.id]))
    elif flag == 1:
        bot.send_message(message.from_user.id, 'Ищу пользователей...')
        if message.from_user.id not in [player_data[0] for player_data in players]:
            players.append([message.from_user.id,message.from_user.first_name])
            if len(players) > 1:
                user1.append([players[0][0],players[0][1]])
                id_pair = user1.index([players[0][0],players[0][1]])
                bot.send_message(user1[id_pair][0], 'Пользователь найден!')
                players.pop(0)
                user2.append([players[0][0],players[0][1]])
                bot.send_message(user2[id_pair][0], 'Пользователь найден!')
                players.pop(0)
                chat(id_pair)
        else:
            pass

def chat(id_pair):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, us1_mes, us2_mes, user1, user2
    user2[id_pair].append([['◻'] * 3 for i in range(3)])
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text='◻', callback_data=f"1{id_pair}")
    b2 = types.InlineKeyboardButton(text='◻', callback_data=f"2{id_pair}")
    b3 = types.InlineKeyboardButton(text='◻', callback_data=f"3{id_pair}")
    b4 = types.InlineKeyboardButton(text='◻', callback_data=f"4{id_pair}")
    b5 = types.InlineKeyboardButton(text='◻', callback_data=f"5{id_pair}")
    b6 = types.InlineKeyboardButton(text='◻', callback_data=f"6{id_pair}")
    b7 = types.InlineKeyboardButton(text='◻', callback_data=f"7{id_pair}")
    b8 = types.InlineKeyboardButton(text='◻', callback_data=f"8{id_pair}")
    b9 = types.InlineKeyboardButton(text='◻', callback_data=f"9{id_pair}")
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    us1_mes = bot.send_message(user1[id_pair][0], f'Играйте! Ты - Нолик! Ты  играешь против {user2[id_pair][1]}! Ты ходишь вторым!',reply_markup=keyboard)
    user1[id_pair].append(us1_mes.id)
    us2_mes = bot.send_message(user2[id_pair][0], f'Играйте! Ты - Крестик! Ты  играешь против {user1[id_pair][1]}! Ты ходишь первым!',reply_markup=keyboard)
    user2[id_pair].append(us2_mes.id)
    user2[id_pair][1] = 1
    user1[id_pair][1] = 0

def chat_bot(id_user):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, us_mes, user_bot
    user_bot[id_user].append([['◻'] * 3 for i in range(3)])
    hod = 0
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text='◻', callback_data=f"1b{id_user}")
    b2 = types.InlineKeyboardButton(text='◻', callback_data=f"2b{id_user}")
    b3 = types.InlineKeyboardButton(text='◻', callback_data=f"3b{id_user}")
    b4 = types.InlineKeyboardButton(text='◻', callback_data=f"4b{id_user}")
    b5 = types.InlineKeyboardButton(text='◻', callback_data=f"5b{id_user}")
    b6 = types.InlineKeyboardButton(text='◻', callback_data=f"6b{id_user}")
    b7 = types.InlineKeyboardButton(text='◻', callback_data=f"7b{id_user}")
    b8 = types.InlineKeyboardButton(text='◻', callback_data=f"8b{id_user}")
    b9 = types.InlineKeyboardButton(text='◻', callback_data=f"9b{id_user}")
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    us_mes = bot.send_message(user_bot[id_user][0], f'Играйте! Ты - Крестик! Ты  играешь против Бота!Ходи первым!', reply_markup=keyboard)
    user_bot[id_user].append(us_mes.id)
    user_bot[id_user].append(0)


    