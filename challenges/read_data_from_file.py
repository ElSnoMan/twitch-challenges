from pprint import pprint

import matplotlib.pyplot as plt

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
    # pandas
    # xlrd

    orders = pd.read_excel('../data/sample_orders.xlsx', sheet_name='Orders')

    # print the whole thing
    orders.plot(x='Item', y='Units', color='red')
    plt.show()
    # pprint(orders)

    # print the values in a column
    # pprint(orders['Rep'].to_list())

    # print the values in a row
    # pprint(orders.iloc[[0]])

    # print the value of a single cell
    # pprint(orders.iloc[[0]]['Rep'])


if __name__ == '__main__':
    # read_csv()
    # read_json()
    read_excel()
