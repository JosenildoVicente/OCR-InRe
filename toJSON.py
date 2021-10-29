import json

def structureJSON(df_texts):

    with open("template.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    result = {}
    for key in jsonObject.keys():
        if key != 'containers':
            result[key] = ""
            re = df_texts[(df_texts.page_num == 0)&((df_texts.centroid_left > jsonObject[key]['left_start']) & (df_texts.centroid_left < jsonObject[key]['left_end'])) & ((df_texts.centroid_top > jsonObject[key]['top_start']) & (df_texts.centroid_top < jsonObject[key]['top_end']))]
            for text in re['text'].values:
                result[key] += text + " "
        else:
            result[key] = 'Não feito ainda'

    res = json.dumps(result, indent = 4)

    return res
