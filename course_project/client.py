from socket import socket, AF_INET, SOCK_STREAM
from time import time
import json
from sys import argv

# для командной строки
# python course_project/client.py localhost 7777

addr = argv[1]
try:
    port = int(argv[2])
except:
    port = 7777

print(addr)
print(port)
s = socket(AF_INET, SOCK_STREAM)

s.connect((addr, port))

while True:
    account_name = input('Введите имя пользователя: ')
    if account_name:
        break
while True:
    user_status = input('Введите статус пользователя: ')
    if user_status:
        break
user = {'account_name': account_name, 'status': user_status}

presence_type = input('Введите тип для presence: ')

presence_data = {'action': 'presence', 'time': time(), 'user': user}

if presence_type:
    presence_data['type'] = presence_type

presence_msg = json.dumps(presence_data).encode('utf-8')

s.send(presence_msg)

#Ответ сервера

server_answer = s.recv(640)

server_data = json.loads(server_answer.decode('utf-8'))

print(f'Данные от сервера: {server_data["alert"]}\n')

s.close()


