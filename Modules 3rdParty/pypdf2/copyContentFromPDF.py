import PyPDF2

# open file
open_file = open('book.pdf', 'rb')
# PdfFileReader object
pdf = PyPDF2.PdfFileReader(open_file)
number_of_pages = len(pdf.pages)
# PdfFileWriter object
writer = PyPDF2.PdfFileWriter()
for i in range(0, number_of_pages):
    # Get the page content
    page = pdf.getPage(i)
    # Extract text from file
    print(page.extract_text())
    # Rotate page content
    page.rotate_clockwise(90)
    # Copying contents
    writer.addPage(page)
# # Copy content will go here
# output_file = open('book-copy.pdf', 'wb')
# # Content pasted in new file
# writer.write(output_file)

# Close files
# output_file.close()
open_file.close()
