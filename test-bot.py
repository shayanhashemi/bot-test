from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from pyrogram.handlers import MessageHandler
from pyrogram import errors
from pyrogram.errors import RPCError
import sqlite3
app = Client("my_account")
me = "@shayann_hashemi"


# async def my_function(client, message):
#     await message.forward(me)

# my_handler = MessageHandler(my_function)
# app.add_handler(my_handler)

Panel_Keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("تنظیم پیام⚙️"), KeyboardButton("تنظیم گروه⚙️")],
    [KeyboardButton("ارسال به مخاطبین📤"), KeyboardButton("ارسال به گروه📤")],
    [KeyboardButton("تنظیم متن ربات➕"), KeyboardButton("تنظیم اکانت")],
    [KeyboardButton("حذف ادمین🗑️"), KeyboardButton("افزودن ادمین➕")],
    [KeyboardButton("دیتابیس💾"), KeyboardButton("ریست ارسالی‌ها🔄")]
], resize_keyboard=True, one_time_keyboard=False)
conn = sqlite3.connect('BotDatabase.db')


def DatabBaseCreator():
    global conn
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER,
            username TEXT,
            name TEXT,
            joined_date TEXT,
            phone_number TEXT,  
            first_time TEXT,
            step TEXT,
            sended TEXT
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY,
            chat_id INTEGER,
            name TEXT
        );
        """
    )
    conn.commit()
    cur.close()


app.run()
