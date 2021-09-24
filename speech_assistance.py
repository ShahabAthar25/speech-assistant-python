from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys

r = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)