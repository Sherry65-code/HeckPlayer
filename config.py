## Configuration file for HeckPlayer
### All the controls that are safe for the user can be used here
#### If you do anything wrong the program will crash. You can fix it by changing the value to default or reinstalling the program
##### Do not remove any of the variables from this file

# Important Imports

from colorama import Fore, Back

# Background colour for widgets
# Options - BLACK, CYAN, RED, GREEN, YELLOW, MAGENTA, WHITE, etc.

BackColor = Back.CYAN

# Text Colour
# Options - BLACK, CYAN, RED, GREEN, YELLOW, MAGENTA, WHITE, etc.

TextColor = Fore.CYAN

# set True if you want the titlebar else set False

showTitleBar = True

# Set progress bar style
# NOTE - progress bar color, if you want it to be default just do progressBarColor = ""

progressBarStyle = " "
progressBarColor = Back.WHITE

# Big Text font
# see all of the options in file fonts.txt

bfont = "rectangles"
