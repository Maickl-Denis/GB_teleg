import os
#pip install python-dotenv
from dotenv import load_dotenv
import ast

#Забирает данные из файла .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
admin_id = os.getenv("admin_id")