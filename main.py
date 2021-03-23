"""Jarvis 0.2"""
import speech_recognition as sr  # Speech recognition (Use Google) (Might not be needed here);
from pynput import keyboard      # Keyboard input listener

# Local imports:
from Jarvis_window import Jarvis_window
from record_and_recognize import record_and_recognise

jarvis_window = Jarvis_window()
r = sr.Recognizer()  # Sound recognizer


def listen_for_request():
    output = record_and_recognise(r)
    jarvis_window.display_text(output)


""" Stuff below literally copy-pasted from https://github.com/moses-palmer/pynput/issues/20 """
# The key combination to check
COMBINATION = {keyboard.Key.ctrl, keyboard.Key.k}

# The currently active modifiers
current = set()


def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            listen_for_request()
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
