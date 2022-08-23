import torch
import sounddevice as sd
import time
# from record import va_listen

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

text = "ноль"

sample_rate = 48000
speaker='baya'
put_accent = True
put_yo = True

audio = model.apply_tts(text=text,speaker=speaker,sample_rate=sample_rate, put_accent=put_accent,put_yo=put_yo)

def play_loop():
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop()

play_loop()