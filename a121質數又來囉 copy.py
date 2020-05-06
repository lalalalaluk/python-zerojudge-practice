import sys
import math

for inputValue in sys.stdin:
    startNumber, endNumber = inputValue.split()

    result = []
    for i in range(int(startNumber), int(endNumber)+1):

        sqrtValue = int(math.sqrt(i))

        isPrime = True
        for j in range(2, sqrtValue+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)

    print(str(len(result)))

