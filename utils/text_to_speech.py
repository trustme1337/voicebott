import aiohttp

async def text_to_speech(text: str, language: str = "ru-RU") -> str:
    from config import YANDEX_API_KEY, YANDEX_FOLDER_ID
    url = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
    headers = {
        "Authorization": f"Api-Key {YANDEX_API_KEY}"
    }
    payload = {
        "text": text,
        "lang": language,
        "voice": "oksana",
        "speed": "1.0",
        "emotion": "neutral",
        "folderId": YANDEX_FOLDER_ID
    }

    audio_path = "output.ogg"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload) as response:
            if response.status == 200:
                with open(audio_path, "wb") as audio_file:
                    audio_file.write(await response.read())
                return audio_path
            else:
                raise Exception(f"Error: {response.status}, {await response.text()}")
