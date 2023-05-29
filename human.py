import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # google speech recognition
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:
        return "None"

    return query.lower()

