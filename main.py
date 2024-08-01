from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F

 #print(message.model_dump_json(indent=4, exclude_none=True)) # - эта строчка позволяет получить апдейт от пользователя

BOT_TOKEN = '7229544704:AAH4F8HNIJVMPMxJqlnGEErPOQXRFZS-syQ'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()




def start_filter(message: Message) -> bool:
    return message.text == '/start'

    



@dp.message(start_filter)
async def start_command(message: Message):
    await message.answer(text='this is commmand start')




if __name__ == '__main__':
    dp.run_polling(bot)



