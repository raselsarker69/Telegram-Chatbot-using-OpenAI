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
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command.
    """
    await message.reply("Hi\nI am Telegram Bot!\nCreated by Rasel sarker. How can I assist you?")


def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    reference.reference = ""


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi there, I'm a ChatGPT Telegram bot created by Rasel sarker! Please follow these commands:

    /start - Start the conversation
    /clear - Clear past conversation and context
    /help  - Show this help menu

    I hope this helps. 🙂
    """
    await message.reply(help_command)


@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the ChatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "assistant", "content": reference.reference},  # previous context
            {"role": "user", "content": message.text}               # current query
        ]
    )

    reference.reference = response['choices'][0]['message']['content']
    print(f">>> ChatGPT: \n\t{reference.reference}")

    await bot.send_message(chat_id=message.chat.id, text=reference.reference)



if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
