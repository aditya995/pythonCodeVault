from PyPDF2 import PdfFileReader, PdfReader

# Using PdfReader
pdfReader_info = PdfReader('book.pdf')
number_of_pages = len(pdfReader_info.pages)
print(number_of_pages)

meta_data = pdfReader_info.metadata

# Using PdfFileReader
PdfFileReader_info = open('book.pdf', 'rb')
pdf_info = PdfFileReader(PdfFileReader_info)
number_of_pages = pdf_info.getNumPages()
print(number_of_pages)

info_gather = pdf_info.getDocumentInfo()
print(info_gather)