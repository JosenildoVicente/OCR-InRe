from getImages import getImages
from getTexts import getTexts

pdf_name = 'A1AA11AA1AA'
pdf_path = 'invoices/Normal/'+pdf_name+'.pdf'

#Convert PDF to Image
pages = getImages(pdf_path, pdf_name)
#Get texts from images
result = getTexts(pages,pdf_name)
print(result)
# print(pages)



# def get_string(img_path,name):
#     # Read image with opencv
#     img = cv2.imread(img_path)

#     # Convert to gray
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply dilation and erosion to remove some noise
#     kernel = np.ones((1,  1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)

#     # Write image after removed noise
#     cv2.imwrite("removed_noise.png", img)
 
#     #  Apply threshold to get image with only black and white
#     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#     # Write the image after apply opencv to do some ...
#     cv2.imwrite("thres.png", img)

#     # Recognize text with tesseract for python
#     result = pytesseract.image_to_data(Image.open("thres.png"))

#     result = result.replace("	",",")

#     # data = io.StringIO(result)
#     # df = pd.read_csv(data, sep=",")

#     # pattern = re.compile(r"\n+( )*")
#     # result = pattern.sub("\n",result)
#     # pattern = re.compile(r"\n+")
#     # result = pattern.sub("\n",result)

#     new_path = name+'.txt'
#     new_days = open(new_path,'w')
#     new_days.write(result)
#     new_days.close()

#     # result = result.split()

#     # Remove template file
#     #os.remove(temp)

#     return result

# print ('--- Start recognize text from image ---')

# texts = get_string( "MXO0505702-1.jpg","MXO0505702-1")
# texts = get_string( "MXO0492981-1.jpg","MXO0492981-1")
# print(texts)MXO0492981
# informacao = {}

# print(texts)

# isvesselInformation = 0
# isVoyageInformation = 0
# isExportInformation = 0

# for num in range(len(texts)):
    # print(text)
    # if isvesselInformation==True:
    #     info = text.split()
    #     tam_info = len(info) - 1
    #     print(info)
    #     informacao['vessel'] = info[tam_info-2] # E mais de uma palavra. Esta incompleta
    #     informacao['port_loading'] = info[tam_info-1]
    #     informacao['port_disclarge'] = info[tam_info]
    #     isvesselInformation = False
        
    # if isVoyageInformation==True:
    #     info = text.split()
    #     print(info)
    #     informacao['voyage_number'] = info[len(info)-1]
    #     isVoyageInformation = False
    
    # if isExportInformation==True:
    #     info = text.split()
    #     print(info)
    #     informacao['export_reference'] = info[len(info)-1]
    #     isExportInformation = False
    # print(texts[num])

    # if (texts[num] == "VOYAGE"):
    #     isVoyageInformation = num
    #     print(isVoyageInformation)

    

    # if (not (text.find("EXPORT") == (-1))):
    #     # print(text)
    #     isExportInformation = True

    # if (not (text.find("VESSEL") == (-1))):
    #     # print(text)
    #     isvesselInformation = True



    

# print(informacao)

# print ("------ Done -------")