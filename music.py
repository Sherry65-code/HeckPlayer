from sys import exit
from dynamics import isThere
from perror import perror

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
