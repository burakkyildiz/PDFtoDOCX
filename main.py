from pdf2docx import Converter

#enter pdf path
pdf_file = r"example.pdf"

#enter output docx path
docx_file = r"example.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()