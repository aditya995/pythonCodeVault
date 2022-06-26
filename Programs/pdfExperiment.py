from PyPDF2 import  PdfReader, PdfWriter

open_file = PdfReader('book.pdf')
writer = PdfWriter()
writer.addPage(open_file.pages[0])
writer.addPage(open_file.pages[1].rotate(90))

page3 = open_file.pages[2]
page3.mediaBox.lower_right = (
    page3.mediaBox.right / 2,
    page3.mediaBox.top / 2
)
writer.addPage(page3)

with open('file.pdf', 'wb')as f:
    writer.write(f)