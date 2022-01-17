import sys
from socket import *
import argparse
import time

from include import protocol
from include.decorators import Log
from include.utils import get_message, send_message
from include.variables import *
from log_configs.client_log_config import get_logger

CLIENT_LOGGER = get_logger()


@Log()
def process_incoming_message(message):
    if RESPONSE in message:
        if message[RESPONSE] == RESPCODE_OK:
            CLIENT_LOGGER.debug('Полученное сообщение ОК')
            return True
        CLIENT_LOGGER.debug('Сервер ответил ошибкой')
        return False
    elif ACTION in message:
        if message[ACTION] == MSG and message[MESSAGE]:
            print(f'{message[FROM]} > {message[MESSAGE]}')
            return True
    raise ValueError


def create_message(user_name):
    message = input('Сообщение:')
    message_full = protocol.CHAT_MSG_CLIENT
    message_full[TIME] = time.time()
    message_full[FROM] = user_name
    message_full[MESSAGE] = message
    return message_full


@Log()
def create_presence(user_name):
    msg = protocol.PRESENCE_MSG_CLIENT
    msg[TIME] = time.time()
    msg[USER][ACCOUNT_NAME] = user_name
    msg[USER][STATUS] = 'Presense status test?'
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение:\n{msg}')
    return msg


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('host', nargs='?', default=DEFAULT_HOST, help='server host ip address')
    parser.add_argument('port', nargs='?', default=DEFAULT_PORT, type=int, help='server port')
    parser.add_argument('-m', action='store', dest='mode', default='listen', help='mode of work')
    parser.add_argument('-u', action='store', dest='user_name', help='mode of work')

    args = parser.parse_args()

    if args.mode not in ('read', 'write'):
        CLIENT_LOGGER.critical('Режим работы не распознан! Поддерживаются только read и write')
        sys.exit(1)

    mode = args.mode
    print(f'Запущен клиент {args.user_name} в {mode} режиме!')

    if not args.user_name:
        user_name = input(f'Введите имя пользователя (default {NOT_LOGGED_USER} - пустое значение):')
        if not user_name:
            user_name = NOT_LOGGED_USER
    else:
        user_name = args.user_name

    with socket(AF_INET, SOCK_STREAM) as client_sock:
        try:
            client_sock.connect((args.host, args.port))
            CLIENT_LOGGER.info(f'Исходящее подключение к серверу: {args.host}:{args.port}')
        except OSError as e:
            CLIENT_LOGGER.critical(e)
            sys.exit(1)

        send_message(client_sock, create_presence(user_name))
        CLIENT_LOGGER.info(f'Отправлено сообщение')
        try:
            answer = get_message(client_sock)
            CLIENT_LOGGER.info(f'Получено сообщение от сервера: {answer}')
            process_incoming_message(answer)
        except ValueError:
            CLIENT_LOGGER.error('Ошибка декодирования сообщения от сервера')

        while True:
            if mode == 'write':
                try:
                    send_message(client_sock, create_message(user_name))
                except:
                    CLIENT_LOGGER.error(f'соединение с сервером разорвано')
                    sys.exit(1)
            if mode == 'read':
                try:
                    process_incoming_message(get_message(client_sock))
                except Exception as e:
                    print(e)
                    CLIENT_LOGGER.error(f'Соединение с сервером разорвано@!!!!!!!')
                    sys.exit(1)


if __name__ == '__main__':
    main()
