from sys import exit
from dynamics import isThere
from perror import perror
from meta import setFileName, getTitle
import ctypes

song = None
songfile = ""
cwd = ""
try:
    from mutagen.mp3 import MP3
except Exception as e:
    perror("mutagen")
#try:
#    from pygame import mixer
#except Exception as e:
#    perror("pygame")

def senddir(dirr):
    global cwd
    cwd = dirr

def play():
    global songfile, lib
    lib.eplay(b"songname.txt")

def pause():
    global lib
    lib.epause()

def nextInQue(si=0, songs=[]):
    if len(songs)-1 == si:
        si = 0
    else:
        si += 1
    setFileName(songs[si])
    return getTitle()

def getSongLength():
    global song
    return song.info.length

def load(musicname=""):
    global song, lib
    if musicname == "":
        # initialize
        lib = ctypes.CDLL(f'{cwd}/easyaudio.so')
        lib.play.argtypes = [ctypes.c_char_p]
        # then exit
        return 0
    else:
        pass
    # load music file
    if isThere(musicname):
        song = MP3(musicname)
        f = open("songname.txt", "w")
        f.write(musicname)
        f.close()
    else:
        return 1

def stop():
    global lob
    lib.estop()

def unpause():
    global lib
    lib.eresume()
