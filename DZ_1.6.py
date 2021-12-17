# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as text_file:
    for i in words:
        text_file.write(i + '\n')


print(locale.getpreferredencoding())

with open('test_file.txt', encoding='utf-8') as text_file:
    for line in text_file:
        print(line, end='')
