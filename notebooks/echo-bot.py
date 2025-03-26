import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
#print(TELEGRAM_BOT_TOKEN)


# configure logging
logging.basicConfig(level=logging.INFO)


# initialize bot and dispatcher
bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)   # synchronized hoy


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help` command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
