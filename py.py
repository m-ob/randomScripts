from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = open('/home/must/Desktop/DBH.pdf','rb')
pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()
x = pdf_reader.getNumPages()
print(x,"\n")
for i in range(0,x,4):
	print(i,"\n")
	pdf_writer.addPage(pdf_reader.getPage(i))
	if (i<220):
		pdf_writer.addPage(pdf_reader.getPage(i+1))

split_file = open('/home/must/Desktop/split.pdf','wb')
pdf_writer.write(split_file)
split_file.close()
pdf_file.close()