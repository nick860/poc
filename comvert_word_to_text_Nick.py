import win32com.client as win32
import os, glob

if __name__=="__main__":
    
    os.chdir("C:\Users\Admin\Desktop")

    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False
    string=""
    for infile in glob.glob(os.path.join('', '*.docx')):
       try:
        doc = word.Documents.Open(os.getcwd()+'\\'+infile)
        text= doc.Range().Text
        string =string +text+"\n"
        work=word.ActiveDocument.SaveAs(infile[:-5]+".txt",FileFormat=win32.constants.wdFormatText)
       except:
           pass
     
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Add()
    word.Visible = True

    rng = doc.Range(0,0)
    rng.InsertAfter(string)
    word.Quit() 
