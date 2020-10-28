import json

def read_data(path='data/production.json'):
    with open(path, encoding='utf-8') as f:
        return  json.load(f)
