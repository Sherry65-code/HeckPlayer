from sys import exit
try:
    import pyfiglet
except Exception as e:
    print("Pyfiglet dosent seems to be installed.")
    exit(1)

def printl(text):
    largetext = pyfiglet.figlet_format(text)
    print(largetext)
