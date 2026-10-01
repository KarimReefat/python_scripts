from docx import Document
from docx.shared import Inches

import os

document = Document('.\\r.docx')

def add_pic2doc(path):
    ''' add the pictures in the path folder to the doc_file.docx file.'''
    a = os.listdir(path)
    a.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)    
    for b in a:
        if b[-3: len(b)] == 'bmp':
            document.add_page_break()
            document.add_picture(path + '\\' + b, width=Inches(7))
    document.add_page_break()
    document.save('.\\r.docx')

def add_many_files(path):
    ''' add all pictures in all the folders in the path to the
        docx files in the same folders '''
    a = [b for b in os.listdir(path) if os.path.isdir(path + '\\' + b)]
    a.sort(key=lambda x: os.stat(os.path.join(path, x)).st_ctime)
    for b in a:
        add_pic2doc(path + '\\' + b)       

add_many_files(r'G:\agc\core 501\research')

