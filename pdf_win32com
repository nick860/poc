import win32com.client
import win32com.client.makepy
import os

win32com.client.makepy.GenerateFromTypeLibSpec('Acrobat')
adobe = win32com.client.DispatchEx('AcroExch.App')
avDoc = win32com.client.DispatchEx('AcroExch.AVDoc')
acroHiList=win32com.client.Dispatch("AcroExch.HiliteList")
acroHiList.Add( 0, 32767 )
ret =avDoc.Open('C:\\Users\\Admin\\Desktop\\nnn.pdf',"Accessing PDF's")

adobe.Show()
avDoc.BringToFront()

pdDoc = avDoc.GetPDDoc()
jso = pdDoc.GetJSObject()
num= pdDoc.GetNumPages()
acroPageView = avDoc.GetAVPageView()
text=""
for page in range(0,num):
    acroPageView.GoTo(page)
    text=text+"\n"+"PAGE: " +str(page)+"\n"
    acroPDPage = acroPageView.GetPage()
    acroPDTextSel = acroPDPage.CreatePageHilite( acroHiList )
    avDoc.SetTextSelection( acroPDTextSel )
    
    for i in range(0,1000):
      try:
       u= acroPDTextSel.GetText(i)
       if len(u)>0:
           text=text+u+""
      except:
          pass


print text
