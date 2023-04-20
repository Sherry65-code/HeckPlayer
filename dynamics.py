from os import system, listdir, name, get_terminal_size
from sys import exit
from random import randint

try:
    from colorama import Fore, Back, Style
except Exception as e:
    print("Run installer file, Module Colorama is not installed or accessible")
    exit(1)

def goToBottom(lines):
    x = 0
    l = getHeight()-lines
    while x<l:
        print()
        x+=1

def setRandomColorBack():
    rn = randint(0, 4)
    if rn == 0:
       print(end=f"{Back.RED}") 
    elif rn == 1:
        print(end=f"{Back.GREEN}")
    elif rn == 2:
        print(end=f"{Back.YELLOW}")
    elif rn == 3:
        print(end=f"{Back.MAGENTA}")
    else:
        print(end=f"{Back.WHITE}")
    print(end=f"{Style.BRIGHT}")

def clearc():
    print(end=f"{Style.RESET_ALL}")

def getSongs():
    curdir = listdir()
    x = 0
    while x<len(curdir):
        if ".mp3" in curdir[x] or ".wav" in curdir[x] or ".m4a" in curdir[x]:
            print(f"{Fore.RED}{Style.BRIGHT}{chr(215)}{Style.RESET_ALL} {curdir[x].split('.')[0]}")
        x+=1

def getSongList():
    curdir = listdir()
    x = 0
    h = 0
    anslist = [""]*len(curdir)
    while x<len(curdir):
        if ".mp3" in curdir[x] or ".wav" in curdir[x] or ".m4a" in curdir[x]:
            anslist[h] = curdir[x]
            h+=1
        x+=1
    return anslist 

def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def isThere(filename):
    curdir = listdir()
    x = 0
    while x<len(curdir):
        if curdir[x] == filename:
            return True
        x+=1
    return False

def getWidth():
    return int(get_terminal_size().columns)

def getHeight():
    return int(get_terminal_size().lines)
