from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, CommandStart
from aiogram.types import Message

from bot_token import BOT_TOKEN
from telegram_id import TELEGRAM_ID



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()






class IsAdmin(BaseFilter):
    def __init__(self, TELEGRAM_ID: list[int]) -> None:
        self.TELEGRAM_ID = TELEGRAM_ID

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.TELEGRAM_ID




@dp.message(IsAdmin(TELEGRAM_ID))
async def answer_if_admins_update(message: Message):
    await message.answer(text="You're admin")

@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text="You're not admin")






if __name__ == '__main__':
    dp.run_polling(bot)



