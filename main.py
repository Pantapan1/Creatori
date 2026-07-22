import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8603618135:AAHbbRy---F5wWuasPoWtHt32w-6Dcr_nyU"
WEBAPP_URL = "https://pantapan1.github.io/my-telegram-app/main.html"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    web_app_info = WebAppInfo(url=WEBAPP_URL)
    
    button = InlineKeyboardButton(
        text="🚀 Открыть приложение",
        web_app=web_app_info
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    
    await message.answer(
        "Привет! 👋\n\nНажми на кнопку, чтобы открыть приложение:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())