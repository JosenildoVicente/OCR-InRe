import cv2
import numpy as np
import pytesseract
from PIL import Image
import pandas as pd
from io import StringIO

def getTexts(pages,name):
    result = []
    for page in pages:
        clearImage(page)
        new_text = recognizeText(page)
        new_df = toDataFrame(new_text)
        df = calculateCentroids(new_df)
        df = sortDataFrame(df)
        result.append(df)
        saveOnAFile(df.to_string(),name)
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

    result = result.replace("	",";")

    return result

def saveOnAFile(text,name):
    
    new_path = name+'.txt'
    new_days = open(new_path,'w')
    new_days.write(text)
    new_days.close()

def toDataFrame(text):
    text_pu = StringIO(text)
    df = pd.read_csv(text_pu,sep=';')
    df = df[df.text.notnull()]
    df = df[df.text.str.isspace()==False]
    return df

def calculateCentroids(df):
    df['centroid_left'] = (df.left + (df.width/2))
    df['centroid_top'] = (df.top + (df.height/2))
    df['centroid_left'] = df['centroid_left'].astype(int)
    df['centroid_top'] = df['centroid_top'].astype(int)
    return df

def sortDataFrame(df):
    df = df.sort_values(by=['centroid_top','centroid_left'])
    return df