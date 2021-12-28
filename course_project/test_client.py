import unittest
import time
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client2 import create_presence, process_ans

# python course_project/test_client.py


class TestClass(unittest.TestCase):
    def test_def_presense(self):
        # проверка create_presence на генерацию правильного запроса присутствия
        right_request = {ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}}
        self.assertEqual(create_presence(), right_request)

    def test_200_ans(self):
        # проверка на правильность разбора ответа 200
        server_answer = {RESPONSE: 200}
        self.assertEqual(process_ans(server_answer), '200 : OK')

    def test_400_ans(self):
        # проверка на правильность разбора ответа 400
        server_answer = {RESPONSE: 400, ERROR: 'Bad Request'}
        self.assertEqual(process_ans(server_answer), '400 : Bad Request')

    def test_no_response(self):
        # проверка корректности срабатывания raise при отсутствии RESPONSE в ответе от сервера
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
