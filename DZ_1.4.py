# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).


words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    byte_word = word.encode('utf-8')
    print(f'Cлово "{word}" в виде байтов: {byte_word}')
    utf_word = byte_word.decode('utf-8')
    print(f'Декодирование "{word}" из байтов: {utf_word}\n')
