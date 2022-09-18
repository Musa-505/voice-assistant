from record import listen
# from speech import play
from append import audio
from package.check_int import check
import command
import answer

import random
import vlc
import os

start = vlc.MediaPlayer("file:///xampp/htdocs/voice-assistant/package/voice_effect/start.m4a")
start.play()
print("All the system worked")

for text in listen():
    if text == command.cmd_exit:
        audio(speack=random.choice(answer.an_cmd))
        quit()
    elif text == command.cmd_grad:
        audio(speack=random.choice(answer.an_grad))
    elif text == command.cmd_check_int:
        audio(speack=check())
    elif text == command.cmd_ply_ms:
        audio(speack=answer.wait)
        os.startfile("C:\Program Files\AIMP\AIMP.exe")
    elif text == command.cmd_ply_mv:
        audio(speack=answer.wait)
        os.startfile("D:\Muvies\Muvie\Bir paytlar Gollivudda 480p O'zbek tilida (asilmedia.net).mp4")
    else:
        print(text)