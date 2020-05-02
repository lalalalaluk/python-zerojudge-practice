import sys

for inputValue in sys.stdin:
    sum = 1
    for i in range(1, int(inputValue)+1):
        sum += int(1 + i * (i - 1) / 2)
    print(str(sum))
