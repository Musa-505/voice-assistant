from secrets import choice
from record import listen
# from speech import play
from append import audio
from package.check_int import check
import random
import command
import answer

for text in listen():
    if text == command.cmd_exit:
        audio(speack=random.choice(answer.an_cmd))
        quit()
    elif text == command.cmd_grad:
        audio(speack=random.choice(answer.an_grad))
    elif text == command.cmd_check_int:
        audio(speack=check())
    
    else:
        print(text)