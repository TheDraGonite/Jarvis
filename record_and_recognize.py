"""This function records and recognizes microphone input"""

import speech_recognition as sr


def record_and_recognise(r: sr.Recognizer) -> str:
    with sr.Microphone() as source:
        print("Слушаю..")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=5)

    try:
        recognized = r.recognize_google(audio, language='ru-RU')
        if type(recognized) == list:
            recognized_string = " ".join(recognized)
            return recognized_string
        else:
            return recognized
    except sr.UnknownValueError:
        print("Unknown sounds came from your mouth. Or perhaps we can't hear you.")
    except sr.RequestError as e:
        print("Sound recognition exception; {0}".format(e))
