
import os 
import PyPDF2 
import pikepdf

# dir_path = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir("encrypted_pdfs"):

    pdf = pikepdf.open('encrypted_pdfs/'+filename)
    
    pdf.save(filename + '_dc')

    print(filename)


