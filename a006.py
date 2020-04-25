from math import *

inputValue = input()

a = int(inputValue.split(' ')[0])
b = int(inputValue.split(' ')[1])
c = int(inputValue.split(' ')[2])

try:
    x1 = int((-b+sqrt((b*b)-(4*a*c)))/(2*a))
    x2 = int((-b-sqrt((b*b)-(4*a*c)))/(2*a))

    if x1 == x2:
        print('Two same roots x=' + str(x1))
    elif x1 > x2:
        print('Two different roots x1='+str(x1)+' , x2='+str(x2))
    elif x2 > x1:
        print('Two different roots x1='+str(x2)+' , x2='+str(x1))
except:
    print('No real root')
