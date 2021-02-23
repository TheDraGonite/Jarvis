"""Джарвис 0.2"""
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("")
    r.pause_threshold=1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    command = r.re