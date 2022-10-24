from struct import calcsize
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
kill_menu = ReplyKeyboardRemove(selective=False)

########################Кнопки#####################
###Общии
OC_button = InlineKeyboardButton(text="Game", callback_data="g_go")
calc = InlineKeyboardButton(text="Калькулятор", callback_data="calc")

########################меню#######################
inline_menu_start = InlineKeyboardMarkup(row_width=2)
inline_menu_start.add(OC_button, calc)



########################calc#######################
but_1 = InlineKeyboardButton(text="1", callback_data="1")
but_2 = InlineKeyboardButton(text="2", callback_data="2")
but_3 = InlineKeyboardButton(text="3", callback_data="3")
but_mul = InlineKeyboardButton(text="*", callback_data="*")

but_4 = InlineKeyboardButton(text="4", callback_data="4")
but_5 = InlineKeyboardButton(text="5", callback_data="5")
but_6 = InlineKeyboardButton(text="6", callback_data="6")
but_del = InlineKeyboardButton(text="/", callback_data="/")

but_7 = InlineKeyboardButton(text="7", callback_data="7")
but_8 = InlineKeyboardButton(text="8", callback_data="8")
but_9 = InlineKeyboardButton(text="9", callback_data="9")
but_skob_open = InlineKeyboardButton(text="(", callback_data="(")

but_minus = InlineKeyboardButton(text="-", callback_data="-")
but_0 = InlineKeyboardButton(text="0", callback_data="0")
but_plus = InlineKeyboardButton(text="+", callback_data="+")
but_skob_clos = InlineKeyboardButton(text=")", callback_data=")")

but_result = InlineKeyboardButton(text="=", callback_data="=")
but_dot = InlineKeyboardButton(text=".", callback_data=".")

inline_menu_calc = InlineKeyboardMarkup(row_width=4)
inline_menu_calc.add(but_1, but_2, but_3, but_mul)
inline_menu_calc.add(but_4, but_5, but_6, but_del)
inline_menu_calc.add(but_7, but_8, but_9, but_skob_open)
inline_menu_calc.add(but_minus, but_0, but_plus, but_skob_clos)
inline_menu_calc.add(but_result, but_dot)