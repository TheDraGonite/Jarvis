"""Джарвис 0.2"""
import pyttsx3
import os
from pocketsphinx import LiveSpeech, get_model_path

engine = pyttsx3.init()  # На всякий случай сделал engine
model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'ru.dic')
)
print("Базарь!")

for phrase in speech:
    print(phrase)
