"""Jarvis window class"""

import playsound
from tkinter import *


class Jarvis_window:
    root = Tk()
    text = Text

    def __init__(self):
        self.root.title("Jarvis listener.")
        Label(self.root, text="Hey, baby! How's it going?").pack()
        Button(self.root, text="!", command=self.on_click).pack()
        self.text = Text(self.root)
        self.text.pack()

        self.hide()

        self.root.mainloop()

    @staticmethod
    def on_click():
        playsound.playsound("resources/start_sound.mp3", True)
        print("This window is non stop.")

    def show(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

    def display_text(self, to_display: str):
        self.text.insert(INSERT, to_display)
        self.text.pack()

