# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
from Speech2Text import Speech2Text
import LUIS


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLING_RATE)
    s = b"".join(data)
    print(type(s))
    wf.writeframes(s)
    wf.close()


def handle_request(filename):
    try:
        text, confidence = Speech2Text(filename)
        print((text, confidence))
        func_name = LUIS.callAPI(text)
        print('Detect function: ', func_name)
    except Exception as e:
        print(e)
    finally:
        print('Finish.')


NUM_SAMPLES = 8000
SAMPLING_RATE = 16000
LEVEL = 3000
COUNT_NUM = 180
SAVE_LENGTH = 2

save_count = 0
save_buffer = []

pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)

while True:
    string_audio_data = stream.read(NUM_SAMPLES)
    audio_data = np.fromstring(string_audio_data, dtype=np.short)
    large_sample_count = np.sum(audio_data > LEVEL)
    print(np.max(audio_data))
    if large_sample_count > COUNT_NUM:
        if save_count == 0:
            print("begin to record")
        save_count = SAVE_LENGTH
    else:
        save_count -= 1

    if save_count < 0:
        save_count = 0
        save_buffer = []
    save_buffer.append(string_audio_data)
    if save_count == 0 and len(save_buffer) > SAVE_LENGTH:
        filename = "a.wav"
        save_wave_file(filename, save_buffer)
        save_buffer = []
        print(filename, "saved")
        handle_request(filename)
        stream.close()
        stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)
