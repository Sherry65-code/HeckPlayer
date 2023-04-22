from sys import exit

def perror(error):
    print(f"{error} not found. Run - pip install -r requirements.txt")
    exit(1)
