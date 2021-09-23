import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "speech.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("hello Tim")