import os
import win32com.client as win32

wordapp = win32.gencache.EnsureDispatch('Word.Application')
wordapp.Visible = False
#doc = wordapp.Documents.Add()
doc = wordapp.Documents.Open(r'F:\test\pics_in_word\New Folder\draft.docx')

def add_pic2doc(path):
    ''' add the pictures in the path folder to the doc_file.docx file.'''
    a = os.listdir(path)
    a.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime, reverse=True)    
    for b in a:
        if b[-3: len(b)] == 'bmp':
            rng = doc.Range(0,0)
            s = "\n" * 30
            rng.InsertAfter(s)
            c = path + '\\' + b
            doc.InlineShapes.AddPicture(c,
                                        False, True
                                        ).ConvertToShape()            

def add_many_files(path):
    ''' add all pictures in all the folders in the path to the
        docx files in the same folders '''
    a = [b for b in os.listdir(path) if os.path.isdir(path + '\\' + b)]
    a.sort(key=lambda x: os.stat(os.path.join(path, x)).st_ctime, reverse=True)
    for b in a:
        add_pic2doc(os.path.abspath(b))    

add_many_files('.\\')

doc.SaveAs(r'F:\test\pics_in_word\New Folder\draft1.docx')
doc.Close()
wordapp.Quit()


