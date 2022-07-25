import json

def get_attr(attr: str):
    with open("config.json", "r") as fp:
        configs = json.loads(fp)
    
    try:
        return configs[attr]
    except KeyError:
        return None
        