from pdf2docx import Converter
pdf_file= 'C:/Users/Riyaj/Desktop/2017ICTS61.pdf'
docx_file='C:/Users/Riyaj/Desktop/2017ICTS61.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()
