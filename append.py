import pyttsx3
def audio(speack):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(speack)
    engine.runAndWait()

audio("Hello")