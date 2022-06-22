# list1 = ['✔', '✔', '✔', ]
# list2 = ['✔', '✔', '✔', ]
# list3 = ['✔', '✔', '✔', ]


# def printli(li: list):
#     for i in li:
#         print(i)


# printli([list1, list2, list3])

# col = int(input('Give column number 1-3\n'))
# row = int(input('Give row number 1-3\n'))
# col -= 1
# row -= 1
# if row == 0:
#     list1[col] = '🎁'
# elif row == 1:
#     list2[col] = '🎁'
# elif row == 2:
#     list3[col] = '🎁'

# printli([list1, list2, list3])

# str = 'sdf'
# str.join()

import pyttsx3
# speaker = pyttsx3.init()
# voice = speaker.getProperty('voices')
# speaker.setProperty('rate', 100)
# speaker.setProperty('voice', voice[1].id)
# speaker.say('gg')
# speaker.runAndWait()


import PyPDF2
from PyPDF2 import PdfFileReader, PdfReader, PdfWriter

# open_file = PdfReader('book.pdf')
# meta_data = open_file.metadata
# print(len(open_file.pages))

# open_file = open('book.pdf', 'rb')
# pdf_info = PdfFileReader(open_file)
# info_gather = pdf_info.getDocumentInfo()
# print(info_gather)

# open_file = open('book.pdf', 'rb')
# pdf = PyPDF2.PdfFileReader(open_file)
# number_of_pages = len(pdf.pages)
# writer = PyPDF2.PdfFileWriter()
# for i in range(0, number_of_pages):
#     page = pdf.getPage(i)
#     page.rotate_clockwise(90)
#     writer.addPage(page)
# output_file = open('book2.pdf', 'wb')
# writer.write(output_file)
# output_file.close()

# encrypts the file
# file_open = PdfReader('book.pdf')
# writer = PdfWriter()
# for page in file_open.pages:
#     writer.addPage(page)

# writer.encrypt('aditya')
# with open('enc.pdf', 'wb') as encrypted:
#     writer.write(encrypted)

## decrypts pdf

# file_open = PdfReader('enc.pdf')
# writer = PdfWriter()
# if file_open.is_encrypted:
#     file_open.decrypt('aditya')
# for page in file_open.pages:
#     writer.addPage(page)

# with open('decrypted.pdf', 'wb') as dy:
#     writer.write(dy)

import pyautogui
for i in range(10):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up