
while 1:
    try:
        inputValue = input()

        k = -7
        resultText = ''

        for i in list(inputValue):
            resultText += chr(ord(i)+k)

        print(resultText)

    except EOFError:
        break
