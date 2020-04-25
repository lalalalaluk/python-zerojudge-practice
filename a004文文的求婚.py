import calendar

while 1:
    try:
        inputYear = input()
    except:
        break

    if calendar.isleap(int(inputYear)):
        print('閏年')
    else:
        print('平年')
