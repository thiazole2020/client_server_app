# Определить, какие из слов «attribute», «класс», «функция»,
# «type» невозможно записать в байтовом типе.

word_1 = b'attribute'
word_2 = b'класс'
word_3 = b'функция'
word_4 = b'type'


# на кирилических словах возникают ошибки вида:
#   SyntaxError: bytes can only contain ASCII literal characters.