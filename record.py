from fileinput import close
import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("model")
samplerate = 16000

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print (res)


va_listen()