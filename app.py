from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys


# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


class Reference:
    """
    A class to store the previous response from the OpenAI API.
    """
    def __init__(self) -> None:
        self.reference = ""


## Create instance of Reference
reference = Reference()
model_name = "gpt-3.5-turbo"



# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Handle /start and /help commands
@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with /start or /help command.
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


# Echo handler - repeats user message
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo.
    """
    await message.answer(message.text)


# Start polling
if __name__ == "__main__":
    executor.start_polling(Dispatcher, skip_updates=True)