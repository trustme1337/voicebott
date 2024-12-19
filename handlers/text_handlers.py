from aiogram import Router
from aiogram.types import Message, FSInputFile
from utils.text_to_speech import text_to_speech
import os

router = Router()

@router.message()
async def handle_text_message(message: Message):
    try:
        audio_file_path = await text_to_speech(message.text, language="ru-RU")
        audio = FSInputFile(audio_file_path)
        await message.answer_voice(audio)
        os.remove(audio_file_path)
    except Exception as e:
        await message.reply(f"Ошибка при обработке текста: {str(e)}")

def register_handlers(dp):
    dp.include_router(router)
