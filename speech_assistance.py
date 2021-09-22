import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    try:
        print(f"You Said: {voice_data}")
    except:
        print("Could not understand")