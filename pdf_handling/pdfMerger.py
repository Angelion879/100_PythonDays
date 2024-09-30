import sys
import PyPDF2

pdf_list = sys.argv
pdf_list.pop(0)

writer = PyPDF2.PdfWriter()

for file in pdf_list:
    with open(f'{file}', 'rb') as current_file:
        reader = PyPDF2.PdfReader(current_file)
        for i in range(len(reader.pages)):
            current_page = reader.pages[i]
            writer.add_page(current_page)

        with open('merged_doc.pdf', 'wb') as new_file:
            writer.write(new_file)