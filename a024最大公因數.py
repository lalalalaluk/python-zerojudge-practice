import sys
import math

for inputValue in sys.stdin:
   number1 , number2 = inputValue.split()
   print(math.gcd(int(number1),int(number2)))
   #最小公倍數
   #print(str(int(int(number1) * int(number2) / math.gcd(int(number1),int(number2)))))
