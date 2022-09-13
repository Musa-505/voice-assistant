from secrets import choice
from record import listen
# from speech import play
from append import audio
import random
import command
import answer

for text in listen():
    if text == command.cmd_exit:
        audio(speack=random.choice(answer.an_cmd))
        quit()
    elif text == command.cmd_grad:
        audio(speack=random.choice(answer.an_grad))
    else:
        print(text)