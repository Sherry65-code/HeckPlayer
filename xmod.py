# To be used for linux

from os import name
from sys import exit

isWindows = False

if name == "posix":
    import Xlib 
    import subprocess

    # get the active window ID using xdotool
    try:
        xdotool_proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE)
    except Exception as e:
        print("Install 'xdotool' using your package manager")
        exit(1)
    window_id = xdotool_proc.stdout.read().strip().decode('utf-8')
    # use the window ID in your program
    your_program_window_id = window_id
else:
    print("This program is not be compatible with Windows. Running it can cause the program to misbehave. If you want to run it then also then press (Y):", end="")
    ui = input()
    if ui.lower() == 'y':
        isWindows = True
    else:
        isWindows = False
        exit(1)

def isFocus():
    global your_program_window_id, isWindows
    if isWindows:
        return True
    else:
        pass
    disp = Xlib.display.Display()
    root = disp.screen().root
    window_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    focused_window = disp.create_resource_object('window', window_id)
    current_window = disp.create_resource_object('window', your_program_window_id)
    return focused_window == current_window

