import pandas as pd
import json


def read_csv():
    animals = pd.read_csv('../data/animals.csv', delimiter=',')
    print(animals.tail(n=1).get('name'))


def read_json():
    # with pandas
    j = pd.read_json('../data/environment.json')
    print(j['staging']['url'])

    # without pandas
    with open('../data/environment.json', 'r') as file:
        _json = json.loads(file.read())

    _json['staging']['url'] = 'foo'
    print(_json['prod'])


def read_excel():
    orders = pd.read_excel('../data/sample_orders.xlsx', sheet_name='Orders')
    print(orders.to_dict())


if __name__ == '__main__':
    # read_csv()
    # read_json()
    read_excel()
