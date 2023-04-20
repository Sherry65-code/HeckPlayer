from music import play, pause, load, stop, unpause, getSongLength
from music import exit as xit
from dynamics import goToBottom, getSongList, clearc, clear, isThere, getWidth, getHeight, setRandomColorBack, Fore, Back, Style, system, getSongs
from time import sleep
from calligraphy import printl


def exit(retcode):
    listener_thread.terminate()
    exit(retcode)

shouldkey = False

try:
    from pynput import keyboard
except Exception as e:
    print("Pynput module not found")
    exit(1)

import threading

def start_listener():
    with keyboard.Listener(on_press=control_playback) as listener:
        listener.join()

def control_playback(key):
    global isPause, shouldkey
    if shouldkey:
        pass
    else:
        return
    if is_terminal_focused():
        pass
    else:
        return
    if key == keyboard.KeyCode.from_char('k'):
        if isPause:
            isPause = False
            unpause()
        else:
            isPause = True
            pause() 
    elif key == keyboard.KeyCode.from_char('s') or key == keyboard.KeyCode.from_char('q'):
        stop()
        clear()
        exit(0)
    else:
        pass
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

isStart=False
isPause=True

clear()
sw = getWidth()
setRandomColorBack()
print("HECKPLAYER", end="")
sw -= 10
x = 0
while x<sw:
    print(end=" ")
    x+=1
clearc()
print()

# intialize
load()

print("All Songs at current directory")
getSongs()

while True:
    try:
        si = int(input("Song index to play:"))
        break
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}NOT A INDEX{Style.RESET_ALL}")
si-=1
try:
    if isThere(getSongList()[si]):
        print(f"Playing {getSongList()[si].split('.')[0]}")
    else:
        print("Song not found!")
        exit(1)
except Exception as e:
    print("Song not found!")
    exit(1)
load(getSongList()[si])
play()
tstart = 0
tmin = 0
# start song
clear()
# then set top
sw = getWidth()
text = f"HECKPLAYER - {getSongList()[si].split('.')[0]}"
lent = sw-len(text)
setRandomColorBack()
x = 0
print(text, end="")
while x<lent:
    print(end=" ")
    x+=1
clearc()
x = 0
th = getHeight()-8
while x<th:
    print()
    x+=1

progressbar=""
lefttime=""
righttime=f" {int(getSongLength()/60)}m:{int(getSongLength()%60)}s"

printl(f"{getSongList()[si].split('.')[0]}")

isPause=False
isStart=True

while tstart<getSongLength():
    try:
        if isPause:
            continue
        else:
            pass
        # SET PROGRESSBAR LENGTH
        lefttime=f"{int(tstart/60)}m:{int(tstart%60)}s  "
        l = len(f"{lefttime}{righttime}")
        remains = getWidth()-l
        progressbar = f"{Back.WHITE}"
        barlength = (tstart/getSongLength())*remains
        x = 0
        while x<barlength-1:
            progressbar+=" "
            x+=1
        progressbar+=f"{Style.RESET_ALL}"
        leftover = remains-barlength
        x=0
        los = ""
        while x<leftover:
            los += " "
            x+=1
        
        if tstart > 59:
            tmin = int(tstart/60)
            tsec = int(tstart%60)
        else:
            tsec = tstart
        print(end=f"\r{lefttime}{progressbar}{los}{righttime}")
        tstart+=1
        sleep(1)
    except KeyboardInterrupt:
        clear()
        print("Exiting")
        stop()
        exit(0)
    except Exception as e:
        clear()
        print(e)
        exit(1)
clear()
exit(0)
