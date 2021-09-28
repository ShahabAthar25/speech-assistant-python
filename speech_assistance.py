from neuralintents import GenericAssistant
from datetime import date, datetime
import speech_recognition as sr
import pyttsx3 as tts
import sys

r = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 130)

todo_list = ['Go Shopping', 'Clean Room']

def create_note():
    global r
    
    speaker.say("What do you want to write onto your note")
    speaker.runAndWait()

    done = False
    
    while not done:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                
                note = r.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename")
                speaker.runAndWait()

                print("Chose Filename")

                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

                filename = r.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as file:
                file.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()
        
        except sr.UnknownValueError:
            r = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()
            print("try again")

def add_todo():
    global r
    
    speaker.say("What todo do you want me to add")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                
                item = r.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"Added {item} to to do list")
                speaker.runAndWait()

        except sr.UnknownValueError:
            r = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()


def show_todo():
     
    speaker.say("The following items are on your todo list")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def current_time():
     
    now = datetime.now()

    current_time = now.strftime("%H %M %S")
    speaker.say(f"The current time is {current_time}")


def greeting():    
    speaker.say("Hello What can i do for you")
    speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
    "greeting": greeting,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todo": show_todo,
    "current_time": current_time,
    "exit": quit
}


assistance = GenericAssistant('intents.json', intent_methods=mappings)
assistance.train_model()

while True:  
    try:

        with sr.Microphone() as source:

            print("speech assistance started")

            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            message = r.recognize_google(audio)
            message = message.lower()

        assistance.request(message)
        print(message)

    except sr.UnknownValueError:
        r = sr.Recognizer()
        speaker.say("Sorry Could Not Understand")
        speaker.runAndWait()