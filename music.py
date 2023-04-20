from sys import exit
from dynamics import isThere

song = None

try:
    from mutagen.mp3 import MP3
except Exception as e:
    print("Install mutagen module")
    exit(1)
try:
    from pygame import mixer
except Exception as e:
    print("Install Pygame module")
    exit(1)

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
