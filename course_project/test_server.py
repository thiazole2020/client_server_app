import unittest
import time
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, RESPONDEFAULT_IP_ADDRESS
from server2 import process_client_message

# python course_project/test_server.py


class TestServer(unittest.TestCase):
    err_dict = {
        RESPONDEFAULT_IP_ADDRESS: 400,
        ERROR: 'Bad Request'
    }

    ok_dict = {
        RESPONSE: 200
    }

    def test_right_request(self):
        # Получение правильного запроса
        right_request = {ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(process_client_message(right_request), self.ok_dict)

    def test_no_action(self):
        # Отсутствие ACTION в запросе
        request_without_action = {TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(process_client_message(request_without_action), self.err_dict)

    def test_wrong_action(self):
        # ACTION из запроса не Presence
        request_with_wrong_action = {ACTION: '????????', TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(process_client_message(request_with_wrong_action), self.err_dict)

    def test_no_time(self):
        # Отсутствие штампа времени
        request_without_time = {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(process_client_message(request_without_time), self.err_dict)

    def test_no_user(self):
        # Отсутствие пользователя в запросе
        request_without_user = {ACTION: PRESENCE, TIME: time.time()}
        self.assertEqual(process_client_message(request_without_user), self.err_dict)

    def test_unknown_user(self):
        # имя пользователя не Guest
        request_user_no_guest = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest?'}}
        self.assertEqual(process_client_message(request_user_no_guest), self.err_dict)


if __name__ == '__main__':
    unittest.main()
