from sys import exit
from colorama import Fore, Style
from dynamics import getRandColor

color = getRandColor(Fore)

try:
    import pyfiglet
except Exception as e:
    print("Pyfiglet dosent seems to be installed.")
    exit(1)

def printl(text):
    largetext = pyfiglet.figlet_format(text)
    print(end=f"{color}{Style.BRIGHT}")
    print(largetext)
    print(end=f"{Style.RESET_ALL}")
