from music import play, pause, load, stop, unpause, getSongLength, nextInQue
from music import exit
from dynamics import setHeader, goToBottom, getSongList, clearc, clear, isThere, getWidth, getHeight,  Fore, Back, Style, printLines, getSongs
from time import sleep
from calligraphy import printl
from sys import argv, stdin
from os import chdir, system, remove
from meta import getTitle, getArtist, getAlbum, setFileName
from gcolor import gcolor
from symbols import loop_on, loop_off
import threading
import config

try:
    from pynput import keyboard
except Exception as e:
    print("pynput module not found")
    exit(1)

paused = False

# Check for arguments count

if len(argv) == 1:
    print("Too less arguments")
    exit(1)
elif len(argv) > 2:
    print("Too many arguments")
    exit(1)
else:
    songloc = argv[1]

# if correct arguments then try changing directory into the specified directory, if director not found then report user

try:
    chdir(songloc)
except Exception as e:
    print("Wrong location")
    exit(1)

# Then display header

clear()
setHeader("HECKPLAYER")

# Then initialize pygame.mixer.music

# intialize
load()

songs = getSongList()

# Then check if songs are avaliable in the spectified directory

if len(songs) == 0:
    print(f"No Song Found in {songloc}")
    exit(0)
else:
    # If avaliable then print all of the songs that contain the .mp3 or .wav or .m4a title
    print("All Songs at current directory")
    getSongs()

# Then ask for song index in the specified list

while True:
    while True:
        try:
            si = int(input("Song index to play:"))
            # then decrement the index inorder to fit the tradition of actual array structers
            si-=1
        except Exception as e:
            print(f"{gcolorb}{Style.BRIGHT}NOT A INDEX{Style.RESET_ALL}")
        except KeyboardInterrupt:
            clear()
            print("Exiting")
            exit(0)

        # Verify song avaliablity
        try:
            if isThere(songs[si]) == False:
                print("Song not found!")
            else:
                break
        except Exception as e:
            print("Song not found!")
    break

prevwidth = getWidth()

def reset():
    global isLoop
    clear()
    # then set header
    setHeader(f"HECKMUSIC - Playing {songname}")
    printLines(getHeight()-14)
    progressbar=""
    lefttime=""
    righttime=f" {int(getSongLength()/60)}m:{int(getSongLength()%60)}s"
    printl(f"{songname}")
    print(f"{gcolor}{Style.BRIGHT}Artist:{Style.RESET_ALL} {songartist}")
    print(f"{gcolor}{Style.BRIGHT}Album:{Style.RESET_ALL}  {songalbum}")
    print(f"{gcolor}{Style.BRIGHT}Next:{Style.RESET_ALL}   {nextInQue(si, songs)}")
    if isLoop:
        loopsymb = loop_on
    else:
        loopsymb = loop_off
    print(f"{gcolor}{Style.BRIGHT}Loop:{Style.RESET_ALL}   {loopsymb}")
    print()

# setting loop variable
isLoop = False

# enabling auto loop end
shouldbreak = False

def nextSong():
    global songs, si, shouldbreak
    if len(songs)-1 == si:
        si = 0
    else:
        si+=1
    shouldbreak = True

def prevSong():
    global songs, si, shouldbreak
    if si == 0:
        si = len(songs)-1
    else:
        si-=1
    shouldbreak = True

runGetKeys = True

def getKeys():
    global paused, runGetKeys, isLoop
    while True:
        if not runGetKeys:
            break
        with keyboard.Events() as events:
            event = events.get(1e6)
            if event.key == keyboard.Key.f7:
                    if paused:
                        reset()
                        unpause()
                        paused = False
                    else:
                        reset()
                        pause()
                        paused = True
            elif event.key == keyboard.Key.f8:
                nextSong()
            elif event.key == keyboard.Key.f6:
                prevSong()
            elif event.key == keyboard.Key.f5:
                if isLoop:
                    isLoop = False
                else:
                    isLoop = True
                reset()
            sleep(0.2)

key_input_thread = threading.Thread(target=getKeys)
key_input_thread.start()

while True:
    # intialize meta package
    setFileName(songs[si])

    # set song arguments
    songname = getTitle()
    songartist = getArtist()
    songalbum = getAlbum()

    # then start playing the song

    maxl = len(songs)
    load(songs[si])
    play()
    tstart = 0
    tmin = 0

    clear()
    # then set header
    setHeader(f"HECKMUSIC - Playing {songname}")
    printLines(getHeight()-14)
    progressbar=""
    lefttime=""
    righttime=f" {int(getSongLength()/60)}m:{int(getSongLength()%60)}s"
    
    printl(f"{songname}")
    print(f"{gcolor}{Style.BRIGHT}Artist:{Style.RESET_ALL} {songartist}")
    print(f"{gcolor}{Style.BRIGHT}Album:{Style.RESET_ALL}  {songalbum}")
    print(f"{gcolor}{Style.BRIGHT}Next:{Style.RESET_ALL}   {nextInQue(si, songs)}")
    if isLoop:
        loopsymb = loop_on
    else:
        loopsymb = loop_off
    print(f"{gcolor}{Style.BRIGHT}Loop:{Style.RESET_ALL}   {loopsymb}")
    print()

    while tstart<getSongLength():
        if getWidth() != prevwidth:
            reset()
            prevwidth = getWidth()
        if shouldbreak:
            break
        if paused:
            sleep(1)
            continue
        try:
            # SET PROGRESSBAR LENGTH
            lefttime=f"{int(round(tstart/60))}m:{round(int(tstart%60))}s  "
            l = len(f"{lefttime}{righttime}")
            remains = getWidth()-l
            progressbar = f"{config.progressBarColor}"
            barlength = int((tstart/getSongLength())*remains)
            x = 0
            for x in range(barlength-1):
                progressbar+=config.progressBarStyle[0]
            progressbar+=f"{Style.RESET_ALL}"
            leftover = remains-barlength
            x=0
            los = ""
            for x in range(leftover):
                los += " "
        
            if tstart > 59:
                tmin = int(tstart/60)
                tsec = int(tstart%60)
            else:
                tsec = tstart
            print(f"{lefttime}{progressbar}{los}{righttime}", end="\r", flush=True)
            tstart+=1
            sleep(1)
        except KeyboardInterrupt:
            runGetKeys = False
            clear()
            print("Exiting")
            stop()
            exit(0)
        except Exception as e:
            clear()
            exit(1)
    # Resetting Break mode
    if isLoop:
        pass
    elif tstart >= int(getSongLength()):
        if si == len(songs)-1:
            si=0
        else:
            si+=1
    shouldbreak = False
