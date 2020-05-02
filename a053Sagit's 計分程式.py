import sys

for inputValue in sys.stdin:
    result = 0
    inputValue = int(inputValue)
    if inputValue <= 10:
        result = str(inputValue * 6)
    elif inputValue > 10 and inputValue <= 20:
        result = str(60 + (inputValue-10) * 2)
    elif inputValue > 20 and inputValue <= 40:
        result = str(80 + (inputValue-20) * 1)
    elif  inputValue > 40:    
        result = 100

    print(str(result))        