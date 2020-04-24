import pandas as pd
import json


animals = pd.read_csv('../data/animals.csv', delimiter=',')
# print(animals.tail(n=1).get('name'))

j = pd.read_json('../data/environment.json')
print(j['staging']['url'])

with open('../data/environment.json', 'r') as file:
    _json = json.loads(file.read())

_json['staging']['url'] = 'foo'
print(_json['prod'])
