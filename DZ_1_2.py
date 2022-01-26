"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
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


def host_range_ping(v_loop_ip):
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


ip_1 = '192.168.2.1'
ip_2 = '192.168.1.253'

ip_1 = ipaddress.IPv4Address(ip_1)
ip_2 = ipaddress.IPv4Address(ip_2)

loop_ip = []


if ip_1 > ip_2:
    ip_2, ip_1 = ip_1, ip_2

v_ip = ip_1

while v_ip <= ip_2:
    loop_ip.append(str(v_ip))
    v_ip = v_ip + 1

host_range_ping(loop_ip)
