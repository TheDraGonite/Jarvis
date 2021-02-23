"""Джарвис 0.2"""
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()  # На всякий случай сделал engine
r = sr.Recognizer()  # Звукоразпознавалка

with sr.Microphone() as source:
    print("Базарь!")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
