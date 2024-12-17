import json

with open('data.json', 'r') as file:
    json_dict = json.load(file)
    json_arr = []
    for key, value in json_dict.items():
        value["ID"] = key
        json_arr.append(value)


def get_plant_dict(class_name:str):
    return json_dict[class_name]

def get_plant_arr():
    return json_arr
