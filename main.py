#pip install pyTelegramBotAPI
import telebot
import Config

bot = telebot.TeleBot(Config.BOT_TOKEN, parse_mode="HTML")


if __name__ == "__main__":
    from handlers import send_to_admin
    send_to_admin()