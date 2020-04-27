import sys

for inputValue in sys.stdin:
    print(int(bin(int(inputValue))[2:]))
