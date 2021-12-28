# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f:
        dict_to_json = json.load(f)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
        print(dict_to_json)

    with open('orders.json', 'w') as f:
        json.dump(dict_to_json, f, indent=4)


write_order_to_json('автомобиль', 2, 1000000, 'Петров', '08.04.2021')
write_order_to_json('автомобиль2', 2, 2000000, 'Петров', '08.04.2021')
