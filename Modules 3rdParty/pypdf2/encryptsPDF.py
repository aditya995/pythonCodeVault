from PyPDF2 import PdfWriter, PdfReader

# encrypts the file
file_open = PdfReader('book.pdf')
writer = PdfWriter()
for page in file_open.pages:
    writer.addPage(page)

writer.encrypt('aditya')
with open('enc.pdf', 'wb') as encrypted:
    writer.write(encrypted)
