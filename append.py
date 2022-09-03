import pyttsx3
def audio(speack):
    engine = pyttsx3.init()
    engine.say(speack)
    engine.runAndWait()