import os
from getImages import getImages
from getTexts import getTexts
from toJSON import structureJSON

def OCRInRe(file_path):
    file_name, file_format = getFileName(file_path)

    pages = getImages(file_path, file_name)

    result = getTexts(pages,file_name)

    new_json = structureJSON(result)

    return new_json

def getFileName(path):
    file = os.path.basename(path)
    file = file.split('.')
    return file[0],file[1]

if __name__ == '__main__':
    OCRInRe(input())