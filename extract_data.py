# importing required modules 
import os 
import PyPDF2 
import pikepdf



# pdf = pikepdf.open('121819_main.pdf')
# pdf.save('extractable.pdf')
  
for filename in os.listdir("encrypted_pdfs"):
    # pdf = pikepdf.open(filename)
    
    # pdf.save(filename + '_dc')

    print(filename)

    # creating a pdf file object 
    pdfFileObj = open(filename, 'rb') 

    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    # printing number of pages in pdf file 
    print(pdfReader.numPages) 

    # creating a page object 
    pageObj = pdfReader.getPage(0) 

    # extracting text from page 
    print(pageObj.extractText()) 

    # closing the pdf file object 
    pdfFileObj.close() 

