from PyPDF2 import PdfMerger

merge_file = PdfMerger()
book = open('book.pdf', 'rb')
journal = open('file.pdf', 'rb')

merge_file.append(fileobj=book, pages=(0, 3))
merge_file.merge(position=1, fileobj=journal, pages=(1, 2))
merge_file.merge(position=3, fileobj=journal, pages=(1, 2))

output = open('merged.pdf', 'wb')
merge_file.write(output)

merge_file.close()
output.close()
