import pyttsx3
import PyPDF2

with open('./book.pdf', 'rb') as book:
    reader = PyPDF2.PdfFileReader(book)

    speaker = pyttsx3.init()
    voice = speaker.getProperty('voices')
    speaker.setProperty('rate', 150)
    speaker.setProperty ('voice', voice[1].id)

    for pageIndex in range(len(reader.pages)):
        pages_to_read = reader.pages[pageIndex]
        text = pages_to_read.extract_text()
        speaker.say(text)
        speaker.runAndWait()