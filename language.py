from langdetect import detect


def detect_language(text: str):

    try:
        lang = detect(text)

        if lang == "ta":
            return "Tamil"

        if lang == "hi":
            return "Hindi"

        return "English"

    except:
        return "English"
