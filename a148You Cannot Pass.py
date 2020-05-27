import sys

for inputValue in sys.stdin:
    scores = inputValue.strip().split(' ')
    scores = [int(i) for i in scores]
    averageScore = sum(scores[1:scores[0]+1]) / (len(scores)-1)
    if averageScore > 59:
        print('no')
    else :
        print('yes')    
