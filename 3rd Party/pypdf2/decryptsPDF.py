from PyPDF2 import  PdfReader, PdfWriter

# decrypts encrypted pdf 

file_open = PdfReader('enc.pdf')
writer = PdfWriter()
if file_open.is_encrypted:
    file_open.decrypt('aditya')
for page in file_open.pages:
    writer.addPage(page)

with open('decrypted.pdf', 'wb') as dy:
    writer.write(dy)