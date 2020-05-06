import sys

for inputValue in sys.stdin:
    ordValue = []
    for i in list(inputValue):
        ordValue.append(ord(i))

    result = ''
    for i in range(0 , len(ordValue[:-2])):
        result += str(abs(ordValue[i] - ordValue[i+1])) 
    print(result)    