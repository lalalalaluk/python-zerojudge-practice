import sys

for inputValue in sys.stdin:
    AtoZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for alphabet in list(AtoZ):
        s = list(alphabet + inputValue)
        if s[0] == 'A':
            s = ['1', '0'] + s
        elif s[0] == 'B':
            s = ['1', '1'] + s
        elif s[0] == 'C':
            s = ['1', '2'] + s
        elif s[0] == 'D':
            s = ['1', '3'] + s    
        elif s[0] == 'E':
            s = ['1', '4'] + s  
        elif s[0] == 'F':
            s = ['1', '5'] + s  
        elif s[0] == 'G':
            s = ['1', '6'] + s  
        elif s[0] == 'H':
            s = ['1', '7'] + s  
        elif s[0] == 'I':
            s = ['3', '4'] + s  
        elif s[0] == 'J':
            s = ['1', '8'] + s  
        elif s[0] == 'K':
            s = ['1', '9'] + s  
        elif s[0] == 'L':
            s = ['2', '0'] + s  
        elif s[0] == 'M':
            s = ['2', '1'] + s  
        elif s[0] == 'N':
            s = ['2', '2'] + s  
        elif s[0] == 'O':
            s = ['3', '5'] + s  
        elif s[0] == 'P':
            s = ['2', '3'] + s  
        elif s[0] == 'Q':
            s = ['2', '4'] + s  
        elif s[0] == 'R':
            s = ['2', '5'] + s  
        elif s[0] == 'S':
            s = ['2', '6'] + s  
        elif s[0] == 'T':
            s = ['2', '7'] + s  
        elif s[0] == 'U':
            s = ['2', '8'] + s  
        elif s[0] == 'V':
            s = ['2', '9'] + s  
        elif s[0] == 'W':
            s = ['3', '2'] + s  
        elif s[0] == 'X':
            s = ['3', '0'] + s  
        elif s[0] == 'Y':
            s = ['3', '1'] + s  
        elif s[0] == 'Z':
            s = ['3', '3'] + s  

        del s[2]

        testResult = 0
        for i in range(1 , 10):
            testResult += int(s[i]) * ( 10 - i )
            
        testResult += int(s[0])  
        testResult += int(s[10])  

        if testResult % 10 == 0:
            result += alphabet

    print(result)        

