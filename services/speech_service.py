from gtts import gTTS
import os

def generate_audio(text, language):

    os.makedirs(
        "data/audio",
        exist_ok=True
    )

    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr"
    }

    audio_path = (
        "data/audio/meme_narration.mp3"
    )

    tts = gTTS(
        text=text,
        lang=lang_map.get(
            language,
            "en"
        )
    )

    tts.save(audio_path)

    return audio_path