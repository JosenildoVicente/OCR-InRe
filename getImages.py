from pdf2image import convert_from_path
import os
#Convert PDF to Image
def getImages(doc,name):
    pages = convert_from_path(doc, 600)
    pagesName = []
    for num in range(len(pages)):
        pagesName.append(name +'-'+ str(num+1) +'.jpg')
        pages[num].save( name +'-'+ str(num+1) +'.jpg', 'JPEG')
    
    return pagesName

def deletImages(pages):
    for i in pages:
        os.remove(i)
