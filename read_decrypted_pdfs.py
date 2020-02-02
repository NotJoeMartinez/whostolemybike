# read the stuff in decryped_pdfs 
import os 
import pprint
import PyPDF2 
import pikepdf

path = 'decrypted_pdfs/'
# this goes through the decrypted_pdf dir and prints out the text of each pdf
for filename in os.listdir("decrypted_pdfs"):
    pdfFileObj = open(path + filename, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0) 
    print(pageObj.extractText()) 

# TO DO: Save extracted text to a text file 

