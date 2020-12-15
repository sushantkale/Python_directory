import os
from PyPDF2 import PdfFileMerger
 
source_dir = os.getcwd()
 
merger = PdfFileMerger()

#select directory where all list of pdfs are store
for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)
 
merger.write('Final_merge_file.pdf')       
merger.close()
