from stt import listen
from tts import say
# from helpers.append import audio
from helpers.date import *
import os

say("Здарсвуите сэр")
say("Все система работаеть")

for text in listen():
    print(text)
    if text == "закончить программа":
        exit()
    elif text == "пока":
        exit()
    elif text == "привет":
        say("привет сэр")
    elif text == "как ты":
        say("здраствуите")
    # turtle command
    elif text == "play music":
        os.startfile("C:\Program Files\AIMP\AIMP.exe")
    elif text == "start mission":
        os.startfile("C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
    # elif text == "starts a web camera":
    #     ok_sir()
    #     os.startfile("C:\Users\ms\Desktop\Camera.lnk")
    # elif text == "start a web camera":
    #     ok_sir()
    #     os.startfile("C:\Users\ms\Desktop\camera.lnk")
    # elif text == "start  web camera":
    #     ok_sir()
    #     os.startfile("C:\Users\ms\Desktop\camera.lnk")
    # current command
    elif text == "current data":
        audio(date2)
    elif text == "current time":
        audio(date2)
    elif text == "time":
        audio(date2)
    else:
        print("Command not found")