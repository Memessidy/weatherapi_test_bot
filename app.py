from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from concurrent.futures import ThreadPoolExecutor
import asyncio
from weather import get_weather as gwf
from tokens import tg_bot_token

_executor = ThreadPoolExecutor(1)
loop = asyncio.get_event_loop()

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Вітаю! Бот запрацював!")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        result = await loop.run_in_executor(_executor, gwf, message.text)
        print(result)
    except Exception as exc:
        print(exc)
    await message.reply(result)


if __name__ == '__main__':
    executor.start_polling(dp)
