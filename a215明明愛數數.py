import sys

for i in sys.stdin:
    startNumber, endValue = i.strip().split(' ')

    count = 1
    sumNumber = int(startNumber)

    while sumNumber <= int(endValue):
        sumNumber += (int(startNumber)+count)
        count += 1

    print(count)
