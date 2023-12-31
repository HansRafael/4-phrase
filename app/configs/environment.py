
import os

class Environment:
    URBAN_DICTIONARY_URI = os.getenv("URBAN_DICTIONARY_URI", "https://mashape-community-urban-dictionary.p.rapidapi.com/define")
    X_RAPID_API_KEY=  os.getenv("X_RAPID_API_KEY", "")
    OXFORD_DICTIONARY_URI = os.getenv("OXFORD_DICTIONARY_URI", "https://www.oxfordlearnersdictionaries.com/definition/english/")
    CAMBRIDGE_DICTIONARY_URI = os.getenv("CAMBRIDGE_DICTIONARY_URI", "https://dictionary.cambridge.org/dictionary/english/")
    BRITANNICA_DICTIONARY_URI = os.getenv("BRITANNICA_DICTIONARY_URI", "https://www.britannica.com/dictionary/")

    PORT = os.getenv("PORT", 8000)
    HOST = os.getenv("HOST", '127.0.0.1')