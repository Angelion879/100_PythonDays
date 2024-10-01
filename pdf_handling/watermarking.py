import os
import sys
import PyPDF2

pdf_list = sys.argv[1:]


def get_file_name(file):
    file_name, old_format = os.path.splitext(file)
    return file_name


def watermark_file(doc, doc_name):
    writer = PyPDF2.PdfWriter()

    with open(f'{doc}', 'rb') as current_file:
        reader = PyPDF2.PdfReader(current_file)

        for i in range(len(reader.pages)):
            content = reader.pages[i]
            content_media = content.mediabox

            with open('wtr.pdf', 'rb') as wtr_mark:
                water_stamp = PyPDF2.PdfReader(wtr_mark)
                stamped_img = water_stamp.pages[0]

                stamped_img.merge_page(content)
                stamped_img.mediabox = content_media
                writer.add_page(stamped_img)

        with open(f'{doc_name}_water.pdf', 'wb') as final:
            writer.write(final)


for pdf in pdf_list:
    pdf_name = get_file_name(pdf)
    watermark_file(pdf, pdf_name)
