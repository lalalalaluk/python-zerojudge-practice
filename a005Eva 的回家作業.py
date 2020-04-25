lineValue = input()

for times in range(int(lineValue)):
    line = input()
    number1 = int(line.split(' ')[0])
    number2 = int(line.split(' ')[1])
    number3 = int(line.split(' ')[2])
    number4 = int(line.split(' ')[3])

    if (number2 - number1 == number3 - number2) and \
            (number3 - number2 == number4 - number3):
        print(line + ' ' + str(number4 + number4 - number3))
    else:
        print(line + ' ' + str(int(number4 * (number4 / number3))))
