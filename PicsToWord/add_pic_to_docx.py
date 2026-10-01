from docx import Document
from docx.shared import Inches

import shutil
import os

def copy_file_to_folders(path, file_name):
    ''' copy the .docx file to the dirctory in that path folder. '''
    a = [b for b in os.listdir(path) if os.path.isdir(
        os.path.join(path,b))]
    for b in a:
        shutil.copy2(file_name, path + '\\' + b)
    
def add_pic2doc(path, doc_file):
    ''' add the pictures in the path folder to the doc_file.docx file.'''
    a = os.listdir(path)
    a.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    document = Document(path + '\\' + doc_file)
    for b in a:
        if b[-3: len(b)] == 'bmp':
            document.add_page_break()
            document.add_picture(path + '\\' + b, width=Inches(7))
    document.save(path + '\\' + doc_file)

def add_many_files(path):
    ''' add all pictures in all the folders in the path to the
        docx files in the same folders '''
    for a in os.listdir(path):
        add_pic2doc(path + '.\\' + a , 'draft.docx')       


copy_file_to_folders(".\\research", 'draft.docx')
add_many_files('.\\research')

