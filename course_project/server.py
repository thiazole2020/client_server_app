from socket import socket, AF_INET, SOCK_STREAM
from time import time
import json
import argparse

# для командной строки
# python course_project/server.py -p 7777

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-p', dest='port', default=7777, type=int)
arg_parser.add_argument('-a', dest='addr', default='')
args = arg_parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)
s.bind((args.addr, args.port))
s.listen(5)

while True:
    client, addr = s.accept()

    client_data = client.recv(640)
    client_msg = json.loads(client_data.decode('utf-8'))

    answer_to_client = {'response': 200, 'time': time(), 'alert': f'ОК. {client_msg["user"]["account_name"]}, Ваше пристутствие зафиксированно'}
    client.send(json.dumps(answer_to_client).encode('utf-8'))

    client.close()