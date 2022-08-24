from record import listen
from speech import play
import command
import answer

for text in listen():
    if text == command.cmd_exit:
        play(text=answer.an_cmd)
        quit()
    elif text == command.cmd_grad:
        play(text=answer.an_grad)
    else:
        print(text)