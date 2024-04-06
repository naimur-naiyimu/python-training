from gtts import gTTS
import os
from googletrans import Translator

def translate_and_pronounce(word):
    translator = Translator()
    
    # Translate English word to Bangla
    translated_text = translator.translate(word, src='en', dest='bn').text
    
    # Print translated text
    print(f"English word: {word}")
    print(f"Bangla meaning: {translated_text}")
    
    # Pronounce Bangla word
    tts = gTTS(translated_text, lang='bn')
    tts.save("pronunciation.mp3")
    os.system("start pronunciation.mp3")

# Example usage:
while True:
    word = input("Enter an English word: ")
    translate_and_pronounce(word)
