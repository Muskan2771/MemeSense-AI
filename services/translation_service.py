from deep_translator import GoogleTranslator

def translate_text(text, language):

    language_map = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr"
    }

    if language == "English":
        return text

    try:
        return GoogleTranslator(
            source="auto",
            target=language_map[language]
        ).translate(text)

    except:
        return text