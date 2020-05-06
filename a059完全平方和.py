import sys
import math

for inputValue in sys.stdin:
    inputGroup  = int(inputValue)

    for i in range(0 , inputGroup):
        result = 0
        startIndex = int(sys.stdin.readline().strip())
        endIndex = int(sys.stdin.readline().strip())

        for j in range (startIndex , endIndex):
            a = int(math.sqrt(j))
            if a * a == j:
                result += j
        print('Case ' + str(i+1) + ': ' + str(result))    