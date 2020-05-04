import sys
import math

for inputValue in sys.stdin:
    startNumber, endNumber = inputValue.split()

    result = []
    for i in range(int(startNumber), int(endNumber)+1):
        if i % 2 == 0 and i != 2:
            continue
        if i % 3 == 0 and i != 3:
            continue
        isPrime = True

        for j in range(5, int(i/2)):
            # print(str(i) + '-'+str(j)+','+str(i % j))
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
    print(' '.join([str(r) for r in result]))
    print(str(len(result)))
