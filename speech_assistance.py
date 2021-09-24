from typing import Mapping
from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys

r = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go Shopping', 'Clean Room']

def print_hello():
    print("Hello")

mappings = {'greeting': print_hello}

assistance = GenericAssistant('intents.json', intent_methods=mappings)
assistance.train_model()

assistance.request("How are you")