import socket
import sys
import os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
BOLD = '\033[1m'
CYAN = '\033[96m'
RESET = '\033[0m'
redfox = f"{BOLD}{RED}RED FOX{RESET}"
dns = f"{BOLD}{GREEN}DNS RESOLVER{RESET}"
seta = f"{GREEN}===========>{RESET}"

banner = f""" {RED}
 __   ___  __      ___  __                __        __      __   ___  __   __                  >
|__) |__  |  \    |__  /  \ \_/    __    |  \ |\ | /__`    |__) |__  /__` /  \ |    \  / |__  |__) 
|  \ |___ |__/    |    \__/ / \          |__/ | \| .__/    |  \ |___ .__/ \__/ |___  \/  |___ |  \ 
                                                                                                   
                                                                                        {RESET} """

print(banner)
print(redfox + " - " + dns)

if len(sys.argv) <= 1:
    print(f"{BOLD}Modo de uso:{RESET}")
    print(f"{BOLD}1 - Python dnsresolver.py google.com{RESET}")
    print(f"{BOLD}2 - Python dnsresolver.py sites.txt{RESET}")
    sys.exit(1)

input_file = sys.argv[1]

if os.path.isfile(input_file):
    with open(input_file, 'r') as file:
        sites = file.readlines()
        for site in sites:
            site = site.strip()  # Remover espaços em branco e quebras de linha
            print(f"{BOLD}{YELLOW}{site}{RESET}", seta, end=' ')
            try:
                ip_address = socket.gethostbyname(site)
                print(f"{BOLD}{CYAN}{ip_address}{RESET}")
            except socket.gaierror:
                print(f"{BOLD}{RED}Erro: Não foi possível resolver o DNS para este site{RESET}")
else:
    site = sys.argv[1]
    print(f"{BOLD}{YELLOW}{site}{RESET}", seta, end=' ')
    try:
        ip_address = socket.gethostbyname(site)
        print(f"{BOLD}{CYAN}{ip_address}{RESET}")
    except socket.gaierror:
        print(f"{BOLD}{RED}Erro: Não foi possível resolver o DNS para este site{RESET}")
print(f"{BOLD}{BLUE}github.com/foxzinnx{RESET}")
