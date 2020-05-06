import sys

for inputValue in sys.stdin:
    totalValue = int(inputValue)

    result = {0:0,1:0,2:0}
    for i in range(0,totalValue):
        result[int(sys.stdin.readline()) % 3]  += 1      
    print(result[0],result[1],result[2])