import sys

for line in sys.stdin:
    line = line.strip()
    if line == line[::-1]:
        print('yes')
    else:
        print('no')
