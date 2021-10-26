

import cv2
import numpy as np
import pytesseract
from PIL import Image


def getTexts(pages):
    result = []
    for page in pages:
        clearImage(page)
        new_text = recognizeText(page)
        result.append(new_text)
        saveOnAFile(new_text,page)
    return result


        
def clearImage(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1,  1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(img_path, img)

def recognizeText(image_path):
    # Recognize text with tesseract for python
    result = pytesseract.image_to_data(Image.open(image_path))

    result = result.replace("	",",")

    return result

def saveOnAFile(text,name):
    
    new_path = name+'.txt'
    new_days = open(new_path,'w')
    new_days.write(text)
    new_days.close()