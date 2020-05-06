import sys

for inputValue in sys.stdin:
    prisoner , redHat = inputValue.split()

    if prisoner == redHat:
        print(prisoner)
    else :
        print(str(int(redHat)+1))