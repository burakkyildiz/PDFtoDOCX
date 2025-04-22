from pdf2docx import Converter

#enter pdf file path
pdf_file = r"example.pdf"

#enter output docx file path
docx_file = r"example.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()