# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
from Speech2Text import Speech2Text
from LUIS import callAPI


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
	text, confidence = Speech2Text(filename)
	print((text, confidence))
	callAPI(text)
	print('Finish.')

NUM_SAMPLES = 2000  # pyAudio内部缓存的块的大小
SAMPLING_RATE = 16000  # 取样频率
LEVEL = 8000  # 声音保存的阈值
COUNT_NUM = 50  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
                 frames_per_buffer=NUM_SAMPLES)

save_count = 0
save_buffer = []

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

    if save_count > 0:
        save_buffer.append(string_audio_data)
    else:
        if len(save_buffer) > 0:
            filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
            save_wave_file(filename, save_buffer)
            save_buffer = []
            print(filename, "saved")
            handle_request(filename)
