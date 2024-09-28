from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.errors import RPCError
app = Client("my_account")
me="@shayann_hashemi"



async def my_function(client, message):
    await message.forward(me)

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)

app.run()