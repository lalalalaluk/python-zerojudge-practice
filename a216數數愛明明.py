import sys

for i in sys.stdin:
    sumFn = 1
    sumGn = 1
    for j in range(2, int(i)+1):
        sumFn += j
        sumGn += sumFn
    print(str(sumFn) + ' ' + str(sumGn))
