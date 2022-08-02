import pyttsx3
speaker = pyttsx3.init()
voice = speaker.getProperty('voices')
speaker.setProperty('rate', 140)
speaker.setProperty('voice', voice[1].id)
speaker.say('I want to write')
speaker.runAndWait()