from os import system, listdir, name, get_terminal_size
from sys import exit
from mutagen.mp3 import MP3
from gcolor import gcolorb, gcolor
from perror import perror

try:
    from colorama import Fore, Back, Style
except Exception as e:
    perror("colorama")


def goToBottom(lines):
    x = 0
    l = getHeight()-lines
    for x in range(l):
        print()

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
    try:
        songn = MP3(songname)
        return songn.info.length
    except Exception as e:
        from pygame import mixer
        mixer.init()
        mixer.music.load(songname)
        return mixer.music.get_length()

def getSongs():
    curdir = listdir()
    x = 0
    h = 0
    for x in range(len(curdir)):
        if ".mp3" in curdir[x] or ".wav" in curdir[x] or ".m4a" in curdir[x]:
            print(f"{gcolor}{Style.BRIGHT}{h+1}.{Style.RESET_ALL} {curdir[x].split('.')[0]} [{int(getSongLength(curdir[x])/60)}m:{int(getSongLength(curdir[x])%60)}s]")
            h+=1

def getSongList():
    curdir = listdir()
    x = 0
    h = 0
    anslist = [""]*len(curdir)
    for x in range(len(curdir)):
        if ".mp3" in curdir[x] or ".wav" in curdir[x] or ".m4a" in curdir[x]:
            anslist[h] = curdir[x]
            h+=1
    return anslist 

def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def isThere(filename):
    curdir = listdir()
    x = 0
    for x in range(len(curdir)):
        if curdir[x] == filename:
            return True
    return False

def getWidth():
    return int(get_terminal_size().columns)

def getHeight():
    return int(get_terminal_size().lines)
