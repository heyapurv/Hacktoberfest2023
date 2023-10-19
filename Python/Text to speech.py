from googletrans import Translator
from gtts import gTTS
import os

# Function to translate text
def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Function to convert translated text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")

if __name__ == "__main__":
    input_text = input("Enter text to translate and convert to speech: ")
    target_language = input("Enter the target language (e.g., 'fr' for French): ")

    translated_text = translate_text(input_text, target_language)
    print(f"Translated Text: {translated_text}")

    text_to_speech(translated_text, target_language)
