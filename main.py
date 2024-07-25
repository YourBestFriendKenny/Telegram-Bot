from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F


BOT_TOKEN = '7229544704:AAH4F8HNIJVMPMxJqlnGEErPOQXRFZS-syQ'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer("Hello, my name is echo-bot, write me someting")



async def process_help_command(message: Message):
    await message.answer("Write me something and i'll reply you your message")





@dp.message()
async def send_echo(message: Message):
    try: 
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=' This type of update is not supported ')





if __name__ == '__main__':
    dp.run_polling(bot)





