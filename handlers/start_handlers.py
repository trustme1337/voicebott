from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Привет! Отправь мне текст, и я преобразую его в голос.")

def register_handlers(dp):
    dp.include_router(router)
