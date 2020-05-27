import sys

for inputValue in sys.stdin:
    totalNumber = int(inputValue)

    for i in range(0, totalNumber):
        result = 1
        number = sys.stdin.readline()
        for j in list(number.strip()):
            result *= int(j)
        print(str(result))
