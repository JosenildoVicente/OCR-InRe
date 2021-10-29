import os
from getImages import getImages, deletImages
from getTexts import getTexts
from toJSON import structureJSON

def OCRInRe(path):
    file_path,file,file_name, file_format = getFileName(path)

    pages = getImages(path, file_name)

    result = getTexts(pages,file_name)

    str_json = structureJSON(result)

    with open(file_path+'/'+file_name+".json", "w") as outfile:
        outfile.write(str_json)

    deletImages(pages)

    return str_json,file,file_path+'/'+file_name+".json"

def getFileName(path):
    file_path = os.path.dirname(path)
    file = os.path.basename(path)
    files = file.split('.')
    return file_path,file,files[0],files[1]

if __name__ == '__main__':
    path = input('Coloque o caminho do arquivo: ')
    my_json,file_name,path_json = OCRInRe(path)
    print(f"Arquivo {file_name} extraido e salvo como: {path_json}")
