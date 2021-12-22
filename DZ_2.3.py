# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
import yaml
from yaml.loader import SafeLoader

data_in_dict = {
    'key_1': [1, 2, 3],
    'key_2': 1,
    'key_3': {
        'key_1.1': '1₿',
        'key_1.2': '3€'
    }
}
with open('file.yaml', 'w', encoding="utf-8") as f:
    yaml.dump(data_in_dict, f, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding="utf-8") as f:
    f_content = yaml.load(f, SafeLoader)

print(data_in_dict)
print(f_content)
if data_in_dict == f_content:
    print('Данные совпадают')
