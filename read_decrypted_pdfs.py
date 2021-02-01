# read the stuff in decryped_pdfs 
import os 
import pprint
import PyPDF2 
import pikepdf

  
def decrypt_pdfs(path, decryped_path):
    for filename in os.listdir(path):
        
        # decrypt pdf
        pdf = pikepdf.open(path+filename)
        pdf.save(decryped_path+filename)

        # read decrypted pdf
        pdfFileObj = open(decryped_path+filename, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

def read_pdfs(decrypted_path):
    # this goes through the decrypted_pdf dir and prints out the text of each pdf
    for filename in os.listdir(decrypted_path):
        pdfFileObj = open(decrypted_path + filename, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0) 
        pdf_text = pageObj.extractText()
        with open("pdf_text/" + filename[:-3] + 'txt', 'w') as writer:
            writer.write(pdf_text)


paths = ['pdfs/2016/', 'pdfs/2017/', 'pdfs/2018/', 'pdfs/2019/', 'pdfs/2020/']

decrypted_path = 'decrypted_pdfs/'

# for path in paths:
#     decrypt_pdfs(path, decrypted_path)

read_pdfs(decrypted_path)


