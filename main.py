import os
import speech_recognition as sr
from AI import MainExe

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query

def WakeUpDetected():
    queery = Listen().lower()

    if "wake up" in queery:
        MainExe()
    else:
        pass


while True:
    WakeUpDetected()