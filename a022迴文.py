import sys

for line in sys.stdin:
    if line == line[::-1]:
        print('true')
    else :
        print('false')    

