from sys import exit
from dynamics import isThere
from perror import perror
from meta import setFileName, getTitle

song = None

try:
    from mutagen.mp3 import MP3
except Exception as e:
    perror("mutagen")
try:
    from pygame import mixer
except Exception as e:
    perror("pygame")

def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

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
    global song
    if musicname == "":
        # initialize
        mixer.init()
        # then exit
        return 0
    else:
        pass
    # load music file
    if isThere(musicname):
        song = MP3(musicname)
        mixer.music.load(f"{musicname}")
    else:
        return 1

def stop():
    mixer.music.stop()

def unpause():
    mixer.music.unpause()
