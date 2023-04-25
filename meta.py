# Controls the metadata

from sys import exit

try:
    import eyed3
except Exception as e:
    print("Eyed3 module not found")
    exit(1)

audio = None
rfilename = None

def setFileName(filename):
    global audio
    try:
        audio = eyed3.load(filename)
    except Exception as e:
        rfilename = filename

def getTitle():
    try:
        return audio.tag.title
    except Exception as e:
        # If the code comes here, then it means the file is not official and its metadata has been removed
        return rfilename.split('.')[0]

def getArtist():
    try:
        return audio.tag.artist
    except Exception as e:
        return "Unknown Artist"

def getAlbum():
    try:
        return audio.tag.album
    except Exception as e:
        return "Unknown Album"
