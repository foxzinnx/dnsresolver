from colorama import Fore, Style, init
import socket
import sys
import argparse

init(autoreset= True)

def main_menu():
    banner = f"""{Fore.RED}
 __   ___  __      ___  __                __        __      __   ___  __   __                  >
|__) |__  |  \    |__  /  \ \_/    __    |  \ |\ | /__`    |__) |__  /__` /  \ |    \  / |__  |__) 
|  \ |___ |__/    |    \__/ / \          |__/ | \| .__/    |  \ |___ .__/ \__/ |___  \/  |___ |  \ 

{Fore.CYAN}github.com/foxzinnx                                                                        
"""
    print(banner)
    print(f"{Fore.RED}{Style.BRIGHT}RED FOX {Style.RESET_ALL}- {Style.BRIGHT}{Fore.GREEN}DNS RESOLVER")


def resolver_wordlist(wordlist):   
    try:
        with open(wordlist, 'r') as file:
            sites = file.readlines()
            print(f"{Fore.GREEN}Resolving DNS for the sites....\n____________________________\n")
            for site in sites:
                site = site.strip() 
                try:
                    ip_address = socket.gethostbyname(site)
                    print(f"{Fore.CYAN}{site}: {Fore.GREEN}{ip_address}")
                except socket.gaierror:
                    print(f"{Fore.RED}{site}: {Style.BRIGHT}Unable to resolve DNS for this site.")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The file {wordlist} was not found.")
        sys.exit(1)

def resolver_target(target):
    print(f"{Fore.GREEN}Resolving DNS for this website: {Fore.LIGHTYELLOW_EX}{target}{Fore.GREEN}\n____________________________\n")
    try:
        ip_address = socket.gethostbyname(target)
        print(f"{Fore.CYAN}{target}: {Fore.GREEN}{ip_address}")
    except socket.gaierror:
        print(f"{Fore.RED}{target}: {Style.BRIGHT}Unable to resolve DNS for this site.")

def main():
    main_menu()

    if len(sys.argv) <= 1:
        print(f"{Style.BRIGHT}Usage:")
        print(f"{Style.BRIGHT}1 - Python dnsresolver.py -t google.com")
        print(f"{Style.BRIGHT}2 - Python dnsresolver.py -w wordlist.txt")
        sys.exit(1)

    parser = argparse.ArgumentParser(description=f"{Fore.RED}RED FOX {Style.RESET_ALL}- {Fore.GREEN}DNS RESOLVER")
    parser.add_argument("-t", "--target", required=False, help=f"{Style.BRIGHT}Target Website")
    parser.add_argument("-w", "--wordlist", required=False, help=f"{Style.BRIGHT}Wordlist file")

    args = parser.parse_args()
    target = args.target
    wordlist = args.wordlist

    if target and wordlist:
        print(f"{Fore.RED}Error: You cannot use both -t and -w arguments simultaneously. Please choose only one.")
        print(f"Example: python dnsresolver.py -t google.com OR python dnsresolver.py -w wordlist.txt")
        sys.exit(1)

    if target:
        resolver_target(target)
    elif wordlist:
        resolver_wordlist(wordlist)
    else:
        print(f"{Style.BRIGHT}Erro: Você deve fornecer um target (-t) ou uma wordlist (-w)")

if __name__ == "__main__":
    main()