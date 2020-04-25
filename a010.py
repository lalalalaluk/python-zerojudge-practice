while 1:
    try:
        intputValue = int(input())

        tmpValue = int(intputValue)
        result = []
        isPrimeNumber = False

        while (not isPrimeNumber):
            if tmpValue > 1:
                stopRun = True
                for j in range(2, tmpValue):
                    if tmpValue % j == 0:
                        tmpValue = int(tmpValue / j)
                        result.append(j)
                        stopRun = False
                        break
                if stopRun:
                    isPrimeNumber = True
            if isPrimeNumber:
                result.append(tmpValue)

        resultText = ''
        resultDict = {}
        for r in result:
            if r in resultDict:
                resultDict[r] = resultDict[r] + 1
            else:
                resultDict[r] = 1

        for key in resultDict:
            if resultDict[key] > 1:
                resultText += str(key) + '^' + str(resultDict[key]) + ' * '
            elif resultDict[key] == 1:
                resultText += str(key) + ' * '

        print(resultText[:-2])
    except EOFError:
        break
