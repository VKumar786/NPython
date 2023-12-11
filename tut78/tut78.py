'''
    TODO: Exercise 8 - Merge the Pdf Solution in Python | Python Tutorial - Day #82 
'''

from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
for i in os.listdir("tut72/"):
    if i.endswith(".pdf"):
        merger.append(open(f"tut72/{i}", "rb"))

with open("tut72/result.pdf", "wb") as fout:
    merger.write(fout)
