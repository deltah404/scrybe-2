import json

def get_attr(attr: str):
    with open("resources/config.json", "r") as fp:
        configs = json.load(fp)
    
    try:
        return configs[attr]
    except KeyError:
        return None
        