import PyPDF2
# import sys

# inputs=sys.argv[1:]

# # with open('dummy.pdf','rb') as file:
# # 	reader=PyPDF2.PdfFileReader(file)
# # 	page=reader.getPage(0)
# # 	page.rotateCounterClockwise(90)
# # 	writer=PyPDF2.PdfFileWriter()
# # 	writer.addPage(page)
# # 	with open('tilt.pdf','wb') as new_file:
# # 		writer.write(new_file)

# def pdf_merger(pdf_list):
# 	merger=PyPDF2.PdfFileMerger()
# 	for pdf in pdf_list:
# 		print(pdf)
# 		merger.append(pdf)
# 	merger.write('super.pdf')
# pdf_merger(inputs)

template=PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
op=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(watermark.getPage(0))
	op.addPage(page)
	with open('watermarked.pdf','wb') as file:
		op.write(file)
