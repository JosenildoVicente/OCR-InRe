import json

def structureJSON(df_texts):

    with open("resposta.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    result = {}
    for key in jsonObject.keys():
        print(key)
        result[key] = ""
        re = df_texts[((df_texts.centroid_left > jsonObject[key]['left_start']) & (df_texts.centroid_left < jsonObject[key]['left_end'])) & ((df_texts.centroid_top > jsonObject[key]['top_start']) & (df_texts.centroid_top < jsonObject[key]['top_end']))]
        for text in re['text'].values:
            result[key] += text

    res = json.dumps(result)

    return res