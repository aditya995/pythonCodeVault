from  PyPDF2 import  PdfWriter, PdfReader

watermark = PdfReader('aditya.pdf')
reader = PdfReader('book.pdf')
writer = PdfWriter()
for i in range(0, len(reader.pages)):
    page = reader.pages[i]
    page.merge_page(watermark.pages[0])
    writer.add_page(page)

with open ('water-marked.pdf', 'wb') as watermarked:
    writer.write(watermarked)