# Controls the metadata

from sys import exit

try:
    import eyed3
except Exception as e:
    print("Eyed3 module not found")
    exit(1)

audio = None

def setFileName(filename):
    global audio
    audio = eyed3.load(filename)

def getTitle():
    return audio.tag.title

def getArtist():
    return audio.tag.artist

def getAlbum():
    return audio.tag.album

