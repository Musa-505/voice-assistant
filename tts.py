import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 24000 # 48000
speaker = 'aidar' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "Привет сэр чем могу помочь?"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)

def say(text):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    print(text)
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

# sd.play(audio, sample_rate * 1.05)
# time.sleep((len(audio) / sample_rate) + 0.5)
# sd.stop()

# print(text)

# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate)
# sd.stop()