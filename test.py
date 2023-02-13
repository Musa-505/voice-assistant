import torch
import sounddevice as sd

def say(say):
    language = "ru"
    model_id = 'v3_1_ru'
    speaker = 'aidar'
    # if langu == 'ru':
    #     model_id = 'v3_1_ru'
    #     speaker = 'aidar'
    # if langu == 'en':
    #     model_id = 'v3_en'
    #     speaker = 'en_73'
    device = torch.device('cpu')
    model, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                                        model='silero_tts',
                                        language=language,
                                        speaker=model_id)
    model.to(device)
    sample_rate = 24000
    example_text = say
    audio = model.apply_tts(text=example_text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=True,
                            put_yo=True)
    sd.play(audio, sample_rate)
    sd.sleep(len(audio) / sample_rate + 0.1)
    sd.stop()

say("Привет")