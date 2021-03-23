"""Proof of concept for Jarvis 0.2."""
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()  # На всякий случай сделал engine
r = sr.Recognizer()  # Звукоразпознавалка

with sr.Microphone() as source:
    print("Слушаю..")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source, phrase_time_limit=5)

try:
    recognized = r.recognize_google(audio, language='ru-RU')
    print("Sphinx thinks you said", recognized)
    if type(recognized) == list:
        recognized_string = " ".join(recognized)
        engine.say(recognized_string)
    else:
        engine.say(recognized)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
