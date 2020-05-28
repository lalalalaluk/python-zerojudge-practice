import sys
import math
import time

for inputValue in sys.stdin:
    tStart = time.time()  # 計時開始
    startNumber, endNumber = inputValue.split()

    result = []
    primeList = []
    lastSqrtValue = 0
    for i in range(int(startNumber), int(endNumber)+1):
    
        sqrtValue = int(math.sqrt(i))

        if lastSqrtValue != sqrtValue and len(primeList) > 0:
            isPrime = True
            lastSqrtValue = sqrtValue
            for j in range(sqrtValue+1, sqrtValue+2):
                # print(str(i) + '-'+str(j)+','+str(i % j))
                primeToAdd = True
                for m in range(2, j):
                    if j % m == 0 and j != m:
                        primeToAdd = False  
                        break
                if primeToAdd:
                    primeList.append(j)

        if len(primeList) > 0 and lastSqrtValue == sqrtValue:
            isPrime = True
            for n in primeList:
                if i % n == 0:
                    isPrime = False
            if isPrime:
                result.append(i)         
        else :
            isPrime = True
            for j in range(2, sqrtValue+1):
                # print(str(i) + '-'+str(j)+','+str(i % j))
                primeToAdd = True
                for m in range(2, j):
                    if j % m == 0 and j != m:
                        primeToAdd = False  
                        break
                if primeToAdd:
                    primeList.append(j)
            for n in primeList:
                if i % n == 0:
                    isPrime = False
            if isPrime:
                result.append(i)  
    # print(' '.join([str(r) for r in result]))
    print(str(len(result)).strip())
    # print(primeList)


