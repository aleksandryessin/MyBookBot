from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

import os

from src.load import load_params

params = load_params()

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN = os.getenv('API_TOKEN')

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                        'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        print(message.json(indent=4, exclude_none=True))
        print(message.json(indent=4, exclude_none=True)[-1])
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                'методом send_copy')


# Навешиваем декоратор без фильтров, чтобы ловить любой тип апдейтов
@dp.message()
async def process_any_update(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришел апдейт
    await message.answer(text='Вы что-то прислали')


if __name__ == '__main__':
    dp.run_polling(bot)
