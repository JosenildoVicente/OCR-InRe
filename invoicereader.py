from getImages import getImages
from getTexts import getTexts
from toJSON import structureJSON

pdf_name = 'MXO0492981'
pdf_path = 'invoices/Normal/'+pdf_name+'.pdf'

#Convert PDF to Image
pages = getImages(pdf_path, pdf_name)

#Get texts from images
result = getTexts(pages,pdf_name)

#Get JSON
new_json = structureJSON(result[0])

print(new_json)

