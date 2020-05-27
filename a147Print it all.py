import sys

for inputValue in sys.stdin:
    print(*[i for i in range(1,int(inputValue)) if i % 7 != 0])