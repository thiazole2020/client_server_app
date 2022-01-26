"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""
import ipaddress
import socket
import os
from platform import system
import subprocess
import chardet


def os_ping(ip_adr):
    oper = system()

    DNULL = open(os.devnull, "w")

    if (oper == "Windows"):
        try:
            res_bytes = subprocess.check_output(f'ping -n 1 {str(ip_adr)}')
            code_dic = chardet.detect(res_bytes)
            res_str = res_bytes.decode(code_dic['encoding']).encode('utf-8')
            res = res_str.decode('utf-8')
            status = res.find('TTL=')
            if status >= 0:
                status = 0
            else:
                status = 1 
        except:
            status = 1
    else:
        status = subprocess.call(["ping", "-c", "1", str(ip_adr)], stdout=DNULL)
    return status


def host_ping(v_loop_ip):
    succes_request = "Узел доступен"
    fail_request = "Узел недоступен"
    fail_ip_adr = "Имя узла задано некорректно"

    columns = ['адрес', 'результат']
    result = []


    i = 0
    for ip in v_loop_ip:
        request_dic = dict()
        try:
            ip_adr = ipaddress.ip_address(ip)
            status = os_ping(ip_adr)
            if status == 0:
                request_dic[columns[0]] = str(ip_adr)
                request_dic[columns[1]] = succes_request
            else:
                request_dic[columns[0]] = str(ip_adr)
                request_dic[columns[1]] = fail_request
        except:
            try:
                ip_adr = socket.gethostbyname(ip)
                status = os_ping(ip_adr)
                if status == 0:
                    request_dic[columns[0]] = str(ip)  
                    request_dic[columns[1]] = succes_request
                else:
                    request_dic[columns[0]] = str(ip) 
                    request_dic[columns[1]] = fail_request
            except:
                request_dic[columns[0]] = str(ip)
                request_dic[columns[1]] = fail_ip_adr
        result.append(request_dic)
        print(f"{result[i][columns[0]]} | {result[i][columns[1]]}")
        i += 1
    return result


loop_ip = ['192.168.1.1', '192.168.1.2', '127.0.0.1', '192.168.0.1', '192.168.1.126', '127', 'google.ru']
host_ping(loop_ip)