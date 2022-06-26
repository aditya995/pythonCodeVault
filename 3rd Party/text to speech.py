import pyttsx3
speaker = pyttsx3.init()
voice = speaker.getProperty('voices')
speaker.setProperty('rate', 140)
speaker.setProperty('voice', voice[0].id)
speaker.say('This is speech test.')
speaker.runAndWait()