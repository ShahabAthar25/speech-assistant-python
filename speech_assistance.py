from typing import Mapping
from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go Shopping', 'Clean Room']

def create_note():
    global recognizer
    
    speaker.say("What do you want to write onto your note")
    speaker.runAndWait()

    done = False
    
    while not done:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as file:
                file.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()
        
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()


def add_todo():
    global recognizer
    
    speaker.say("What todo do you want me to add")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                
                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"Added {item} to to do list")
                speaker.runAndWait()

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()


def show_todo():
     
     speaker.say("The following items are on your todo list")
     for item in todo_list:
         speaker.say(item)
     speaker.runAndWait()


def greeting():    
    speaker.say("Hello What can i do for you")
    speaker.runAndWait()


assistance = GenericAssistant('intents.json')
assistance.train_model()