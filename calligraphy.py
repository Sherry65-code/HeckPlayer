from sys import exit
from colorama import Fore, Style
from gcolor import gcolor
from perror import perror

color = gcolor

prev = ""
prevs = ""

try:
    import pyfiglet
except Exception as e:
    perror("pifiglet")

def printl(text):
    global prev, prevs
    if text == prevs:
        largetext = prev
    else:
        largetext = pyfiglet.figlet_format(text)
    print(end=f"{gcolor}{Style.BRIGHT}")
    print(largetext)
    print(end=f"{Style.RESET_ALL}")
    prev = largetext
    prevs = text
    return largetext
