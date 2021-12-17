# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess

resourses = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for args in resourses:
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        print(line.decode('cp866').encode('utf-8').decode('utf-8'))