from record import listen
# from speech import play
from append import audio
import command
import answer

for text in listen():
    if text == command.cmd_exit:
        audio(speack=answer.an_cmd)
        quit()
    elif text == command.cmd_grad:
        audio(speack=answer.an_grad)
    else:
        print(text)