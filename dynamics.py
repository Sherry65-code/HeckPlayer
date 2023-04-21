from os import system, listdir, name, get_terminal_size
from sys import exit
from mutagen.mp3 import MP3
from gcolor import gcolorb, gcolor

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

def printLines(num):
    x = 0
    for x in range(num):
        print()

def setHeader(headline):
    print(end=f"{gcolorb}{Style.BRIGHT}")
    print(end=headline)
    l = len(headline)
    tl = getWidth()
    l = tl-l
    x = 0
    for x in range(l):
        print(end=" ")
    print()
    clearc()

def clearc():
    print(end=f"{Style.RESET_ALL}")

def getSongLength(songname):
    songn = MP3(songname)
    return songn.info.length

def getSongs():
    curdir = listdir()
    x = 0
    h = 0
    while x<len(curdir):
        if ".mp3" in curdir[x] or ".wav" in curdir[x] or ".m4a" in curdir[x]:
            print(f"{gcolor}{Style.BRIGHT}{h+1}.{Style.RESET_ALL} {curdir[x].split('.')[0]} [{int(getSongLength(curdir[x])/60)}m:{int(getSongLength(curdir[x])%60)}s]")
            h+=1
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
