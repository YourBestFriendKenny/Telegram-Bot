from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, CommandStart
from aiogram.types import Message
from w_sourse.bot_token import BOT_TOKEN
from w_sourse.bot_token import TELEGRAM_ID



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

admin_ids: list[int] = [TELEGRAM_ID]






if __name__ == '__main__':
    dp.run_polling(bot)



