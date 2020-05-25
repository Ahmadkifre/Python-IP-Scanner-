import requests
import colorama
import time
from colorama import Fore
class colors:
    black = Fore.LIGHTBLACK_EX
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.LIGHTCYAN_EX
    green = Fore.LIGHTGREEN_EX
    magenta = Fore.LIGHTMAGENTA_EX
    red = Fore.LIGHTRED_EX
    white = Fore.LIGHTWHITE_EX
    yellow = Fore.LIGHTYELLOW_EX
c = colors()
banner = c.cyan + """

                |\/\/\/|  
                |      |  
                | (o)(o)  
                C      _) 
                |  ___|  
                 |   /    
                /____\    
               /      \


            [*] Cyber Shield [*]  
             ~ Ahmad A Abdulla :)
"""

print(banner)


def menu():
    print("1: Reverse Ip Lookup")
    print("2: Ip scaner")
    choice = input()
    if choice == 1:
       reverse()
   
    else:  
        if choice==2:
          nmap()


def reverse():
    ip = raw_input("Enter IP address: ")
    r = requests.get('http://api.hackertarget.com/reverseiplookup/?q=' + ip)
    if r.status_code == 200:
         print(ip)
         if "error" in r.text :
             print("Error IP address")
         else:
              print(r.text)
    else:
            print("Error")



def nmap():
    ip = raw_input("Enter IP address: ")
    r = requests.get('https://api.hackertarget.com/nmap/?q=' + ip)
    if r.status_code == 200:
         print(ip)
         if "error" in r.text :
             print("Error IP address")
         else:
              print(r.text)
    else:
            print("Error")

menu()


