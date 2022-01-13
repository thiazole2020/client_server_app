from include.variables import *

# Шаблон Presence сообщения протокола JIM
PRESENCE_MSG_CLIENT = {
    ACTION: PRESENCE,
    TIME: None,
    TYPE: STATUS,
    USER: {
        ACCOUNT_NAME: NOT_LOGGED_USER,
        STATUS: None
    }
}
# Шаблон успешного ответа
SERVER_RESPONSE_OK = {
    RESPONSE: RESPCODE_OK,
    ALERT: RESPONSE_OK_TEXT
}
# Шаблон неуспешного ответа (400, bad request)
SERVER_RESPONSE_BAD_REQUEST = {
    RESPONSE: RESPCODE_BAD_REQ,
    ALERT: RESPONSE_BAD_REQUEST_TEXT
}
# Шаблон неуспешной ответа (500, ошибка сервера)
SERVER_RESPONSE_SERVER_ERROR = {
    RESPONSE: RESPCODE_SERVER_ERROR,
}