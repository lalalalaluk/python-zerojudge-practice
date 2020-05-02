import sys

for i in sys.stdin:
    startNumber , endNumber = i.split()

    result = ''
    for includedNumber in range(int(startNumber),int(endNumber)):
        addNumber = 0
        for splitN in list(str(includedNumber)):
            addNumber += int(splitN)**len(list(str(includedNumber)))

        if addNumber == includedNumber:
            result +=  str(addNumber) + ' ' 

    if result:
        print(result)
    else :
        print('none')    

