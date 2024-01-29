import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime
import webbrowser

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    subprocess.run(["afplay", "output.mp3"])

def open_url(url):
    webbrowser.open(url)

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    open_url(search_url)

def youtube_search(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    open_url(search_url)

if __name__ == "__main__":
    trigger_word = "hi"

    while True:
        print("Listening for trigger word...")
        trigger = listen()

        if trigger_word in trigger:
            speak("How can I assist you today?")
            
            while True:
                query = listen()

                if "hello" in query:
                    speak("Hi there! How can I help you?")
                elif "bye" in query:
                    speak("Goodbye! Have a great day.")
                    break
                elif 'time' in query:
                    current_time = datetime.datetime.now().strftime('%H:%M')
                    speak(f"The current time is {current_time}")
                elif 'google' in query:
                    search_query = query.replace('google', '')
                    google_search(search_query)
                elif 'youtube' in query:
                    search_query = query.replace('youtube', '')
                    youtube_search(search_query)
                elif trigger_word in query:
                    break  # Break out of the inner loop and wait for the trigger word again
                else:
                    speak("I'm sorry, I didn't understand that. Could you please repeat?")
