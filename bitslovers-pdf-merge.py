import PyPDF2 
import sys

filesList = sys.argv

# Create a new Object PdfFileWriter as blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the all files specified on Arguments and then Iterate over all pages for each PDF file
for i in range(1, len(filesList)):
    pdfFile = open(filesList[i], 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutput = open('bitslovers-merged.pdf', 'wb')
pdfWriter.write(pdfOutput)
 
# Close all the files
pdfOutput.close()
pdfFile.close()
