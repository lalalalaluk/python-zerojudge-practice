import sys

for inputValue in sys.stdin:
    sortNumber = int(inputValue)

    listValue = sys.stdin.readline().split()
    result = sorted([int(l) for l in listValue])
    print(' '.join([str(r) for r in result]))
