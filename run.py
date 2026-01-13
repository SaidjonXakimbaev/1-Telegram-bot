import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Assalomu alaykum {message.from_user.full_name}!\n\n"
        f"Bu mening birinchi Telegram Botim\n"
        f"Ustozim Nodir Ustoz\n"
        f"Men kelajakda kuchli dasturchi bo'lmoqchiman!"
    )

@dp.message(F.text == "Assalomu alaykum")
async def cmd_salom(message: Message):
    await message.answer(
        f"Valeykum assalom, Assalomu alaykum!"
    )

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply(
        f"Sizga qanday yordam kerak?\n\n"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Siz klaviatura yordamida dasturni to'xtatdingiz!\nGoodbye")