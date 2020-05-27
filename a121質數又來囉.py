import sys
import math
import time

for inputValue in sys.stdin:
    tStart = time.time()  # 計時開始
    startNumber, endNumber = inputValue.split()

    result = []
    for i in range(int(startNumber), int(endNumber)+1):
        isPrime = True
        if i % 2 == 0:
            continue
        if i % 3 == 0:
            continue
        if i % 5 == 0:
            continue
        if i % 7 == 0:
            continue
        if i % 11 == 0:
            continue

        for j in range(2, int(math.sqrt(i))):
            # print(str(i) + '-'+str(j)+','+str(i % j))
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
    # print(' '.join([str(r) for r in result]))
    tEnd = time.time()  # 計時結束
    print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位
    print(str(len(result)))
