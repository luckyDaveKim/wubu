import json


def dataframe2json(dataframe):
    json_string = dataframe.to_json(orient='records')
    json_data = json.loads(json_string)
    return json_data
