import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import start_handlers, text_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():
    start_handlers.register_handlers(dp)
    text_handlers.register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
